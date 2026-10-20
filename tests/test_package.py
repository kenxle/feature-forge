import contextlib
import importlib.util
import io
import os
import re
import subprocess
from pathlib import Path
import shutil
import tempfile
import unittest
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
STYLE_FIXTURE = ROOT / 'tests/fixtures/house-style'
NO_STYLE = {}
WITH_STYLE = {'FORGE_DOC_STYLE_DIR': str(STYLE_FIXTURE)}

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

installer = module('installer', ROOT / 'scripts/install.py')
layout = module('layout', ROOT / 'skills/feature-forge/scripts/doc_layout.py')
renderer = module('renderer', ROOT / 'skills/feature-forge/scripts/build_feature_docs.py')
support = module('support', ROOT / 'skills/feature-forge/scripts/forge_support.py')

class PackageTest(unittest.TestCase):
    def build_quietly(self, folder, environ):
        with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
            return renderer.build(folder, environ)

    def test_evidence_reports_failure_and_preserves_prior_run(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            evidence = root / 'evidence'
            status = support.verify(root, evidence, [sys.executable, '-c',
                'print("actual output"); raise SystemExit(7)'])
            self.assertEqual(status, 7)
            self.assertIn('actual output', (evidence / 'output.log').read_text())
            self.assertEqual(json.loads((evidence / 'result.json').read_text())['exit_code'], 7)
            with self.assertRaises(ValueError):
                support.verify(root, evidence, [sys.executable, '-c', 'pass'])

    def test_local_markdown_links_exist(self):
        import re
        for source in ROOT.rglob('*.md'):
            if '.git' in source.parts:
                continue
            # Frozen upstream review sources retain their original examples and
            # links to unselected files. Package files never use this exemption.
            if source.is_relative_to(ROOT / 'docs') and any(
                    (parent / '.source-archive').is_file()
                    for parent in source.parents if parent.is_relative_to(ROOT)):
                continue
            for target in re.findall(r'\]\(([^)]+)\)', source.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                self.assertTrue((source.parent / target.split('#')[0]).exists(),
                                str(source) + ': ' + target)

    def test_safe_install_and_conflict(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            installer.install(root, True)
            self.assertFalse((root / '.claude').exists())
            installer.install(root)
            installed = root / '.claude/skills'
            self.assertEqual(set(p.name for p in installed.iterdir()), set(installer.NAMES))
            marker = installed / 'brief/SKILL.md'
            marker.write_text('local edit')
            with self.assertRaises(ValueError):
                installer.install(root)
            self.assertEqual(marker.read_text(), 'local edit')
            # The fresh installed copy has all renderer assets available.
            fresh = module('installed_renderer', installed / 'feature-forge/scripts/build_feature_docs.py')
            self.assertTrue(fresh.HEADER.exists())
            self.assertTrue(fresh.HOUSE_HEADER.exists())
            for helper in ('doc_style.py', 'doc_layout.py'):
                self.assertTrue((installed / 'feature-forge/scripts' / helper).is_file())
            self.assertTrue((installed / 'feature-forge/references/principles.md').is_file())
            self.assertTrue((installed / 'feature-forge/vendor/pstack/LICENSE').is_file())
            self.assertTrue(list((installed / 'feature-forge/vendor/pstack/skills').glob('principle-*/SKILL.md')))

    def test_include_containment_cycle_missing(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            doc = root / 'doc.md'
            doc.write_text('<!-- forge-include: doc.md -->')
            with self.assertRaisesRegex(ValueError, 'cycle'):
                renderer.expand(doc, root)
            doc.write_text('<!-- forge-include: ../outside.md -->')
            with self.assertRaisesRegex(ValueError, 'escapes'):
                renderer.expand(doc, root)
            doc.write_text('<!-- forge-include: missing.md -->')
            with self.assertRaises(FileNotFoundError):
                renderer.expand(doc, root)

    @unittest.skipUnless(shutil.which('pandoc'), 'Optional Pandoc not installed')
    def test_dossier_composition(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'example'
            shutil.copytree(ROOT / 'tests/fixtures/csv-export', root)
            pages = self.build_quietly(root, NO_STYLE)
            brief = (root / '01_brief_csv-export.html').read_text()
            self.assertIn('CSV quoting', brief)
            self.assertIn('Review history', brief)
            self.assertIn('03_plan_csv-export.html', brief)
            self.assertNotIn('forge-include:', brief)
            self.assertNotIn('<script', brief)
            self.assertEqual(len(pages), 4)

    @unittest.skipUnless(shutil.which('pandoc'), 'Optional Pandoc not installed')
    def test_prototype_first_dossier_keeps_plan_progress_and_reviews(self):
        names = ('01_brief', '02_prototype', '03_prd', '04_architecture',
                 '05_plan', '06_progress')
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            for name in names:
                (folder / (name + '.md')).write_text('# ' + name + '\n')
            (folder / '03_prd.md').write_text('# Requirements\n\n[Plan](05_plan.md)\n')
            (folder / '05_plan_reviews.md').write_text('Independent testing findings\n')
            (folder / 'README.md').write_text('Not a numbered dossier page\n')
            pages = self.build_quietly(folder, NO_STYLE)
            self.assertEqual({page.stem for page in pages}, set(names))
            for page in pages:
                output = page.read_text()
                for name in names:
                    self.assertIn('href="' + name + '.html"', output)
            self.assertIn('Independent testing findings', (folder / '05_plan.html').read_text())
            self.assertIn('href="05_plan.html"', (folder / '03_prd.html').read_text())

@unittest.skipUnless(shutil.which('pandoc'), 'Optional Pandoc not installed')
class HouseStyleTest(unittest.TestCase):
    """The built dossier must carry the house document style when it exists.

    These tests use a made-up style folder (tests/fixtures/house-style), never
    a real style. They fail if the renderer stops inlining the style or stops
    writing the layout the style expects.
    """

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def build(self, folder, environ):
        err = io.StringIO()
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            pages = renderer.build(folder, environ)
        return pages, err.getvalue()

    def csv_export(self, environ):
        folder = self.root / 'csv-export'
        shutil.copytree(ROOT / 'tests/fixtures/csv-export', folder)
        pages, err = self.build(folder, environ)
        return folder, pages, err

    def test_page_inlines_the_style_for_the_switcher(self):
        folder, _, err = self.csv_export(WITH_STYLE)
        page = (folder / '01_brief_csv-export.html').read_text()
        self.assertEqual(err, '')
        self.assertEqual(page.count('<style data-lahe-doc-style>'), 1)
        self.assertIn('FIXTURE-STYLE-TOKENS', page)
        self.assertIn('.insight { border-left', page)
        self.assertNotIn('@import url("system-tokens.css")', page)
        self.assertLess(page.index('data-lahe-doc-style'), page.index('<body>'))

    def test_page_uses_the_layout_the_style_expects(self):
        folder, _, _ = self.csv_export(WITH_STYLE)
        page = (folder / '01_brief_csv-export.html').read_text()
        self.assertIn('<div class="hero">', page)
        self.assertIn('<nav class="toplinks" aria-label="Documents">', page)
        self.assertIn('<span aria-current="page">Brief</span>', page)
        self.assertIn('href="03_plan_csv-export.html"', page)
        self.assertIn('<details class="fold contents" open>', page)
        self.assertIn('<nav id="TOC" class="contents-list">', page)
        self.assertIn('<section class="sheet">', page)
        self.assertIn('<span class="n">Section 1</span>', page)
        self.assertIn('<span class="n">Section 3</span>', page)
        self.assertIn('Review history', page)
        self.assertIn('class="reviews-banner"', page)
        self.assertNotIn('forge-include:', page)

    def test_house_page_stays_offline(self):
        folder, _, _ = self.csv_export(WITH_STYLE)
        for page in folder.glob('*.html'):
            text = page.read_text()
            self.assertNotIn('<script', text)
            self.assertNotRegex(text, r'(?:src|href)="https?://')

    def test_house_components_render_styled(self):
        folder = self.root / 'components'
        folder.mkdir()
        (folder / '01_page.md').write_text(
            '# Component page\n\nThe lede.\n\n## Findings\n\n'
            '<div class="insight">\n\nAn insight panel.\n\n</div>\n\n'
            '<div class="xref">See <a href="02_other.md#x">the other page</a></div>\n\n'
            '::: callout-question\nIs this still open?\n:::\n\n'
            '- [x] done item\n\n## 2. Second\n\nMore.\n')
        (folder / '01_page_reviews.md').write_text(
            '## Architect Review\n\n**RF1: a finding**\n\n'
            '| # | Verdict |\n|---|---|\n| RF1 | Accepted |\n| RF2 | Rejected |\n'
            '| RF3 | Deferred |\n')
        (folder / '02_other.md').write_text('# Other\n\nBody.\n')
        self.build(folder, WITH_STYLE)
        page = (folder / '01_page.html').read_text()
        self.assertIn('<div class="insight">', page)
        self.assertIn('class="xref"', page)
        self.assertIn('href="02_other.html#x"', page)
        self.assertIn('insight insight--caveat', page)
        self.assertIn('data-label="Open question"', page)
        self.assertIn('status-dot status-dot--sage">Accepted', page)
        self.assertIn('status-dot status-dot--purple">Rejected', page)
        self.assertIn('status-dot status-dot--faint">Deferred', page)
        self.assertIn('<a href="#architect-rf1">RF1</a>', page)
        self.assertIn('<p class="lede">The lede.</p>', page)
        self.assertIn('<span class="n">Section 2</span>', page)
        self.assertIn('type="checkbox"', page)
        self.assertIn('<div class="scrollx"><table', page)

    def test_fonts_the_style_names_are_copied_beside_the_pages(self):
        folder, _, _ = self.csv_export(WITH_STYLE)
        font = folder / '.lahe-fonts' / 'fixture-font.woff2'
        self.assertEqual(font.read_bytes(), (STYLE_FIXTURE / 'fonts/fixture-font.woff2').read_bytes())

    def test_the_variable_beats_lahe_on_path(self):
        clone = self.make_lahe_clone('wrapper')
        other = self.root / 'other-style'
        shutil.copytree(STYLE_FIXTURE, other)
        (other / 'document.css').write_text(
            (other / 'document.css').read_text() + '\n/* THE-VARIABLE-STYLE */\n')
        folder = self.root / 'csv-export'
        shutil.copytree(ROOT / 'tests/fixtures/csv-export', folder)
        self.build(folder, {'PATH': str(clone['bin']), 'FORGE_DOC_STYLE_DIR': str(other)})
        page = (folder / '01_brief_csv-export.html').read_text()
        self.assertIn('THE-VARIABLE-STYLE', page)

    def make_lahe_clone(self, kind):
        clone = self.root / ('clone-' + kind)
        shutil.copytree(STYLE_FIXTURE, clone / 'vendor/stclair-doc-style')
        (clone / 'bin').mkdir()
        launcher = clone / 'bin/lahe.js'
        launcher.write_text('// stands in for the real launcher\n')
        bindir = self.root / ('bin-' + kind)
        bindir.mkdir()
        command = bindir / 'lahe'
        if kind == 'wrapper':
            command.write_text('#!/bin/sh\nexec "node" "' + str(launcher) + '" "$@"\n')
            command.chmod(0o755)
        else:
            command.symlink_to(launcher)
            launcher.chmod(0o755)
        return {'bin': bindir}

    def test_lahe_found_through_its_wrapper_script(self):
        clone = self.make_lahe_clone('wrapper')
        folder = self.root / 'csv-export'
        shutil.copytree(ROOT / 'tests/fixtures/csv-export', folder)
        _, err = self.build(folder, {'PATH': str(clone['bin'])})
        self.assertEqual(err, '')
        self.assertIn('FIXTURE-STYLE-TOKENS', (folder / '01_brief_csv-export.html').read_text())

    def test_lahe_found_through_a_symlinked_command(self):
        clone = self.make_lahe_clone('symlink')
        folder = self.root / 'csv-export'
        shutil.copytree(ROOT / 'tests/fixtures/csv-export', folder)
        _, err = self.build(folder, {'PATH': str(clone['bin'])})
        self.assertEqual(err, '')
        self.assertIn('FIXTURE-STYLE-TOKENS', (folder / '01_brief_csv-export.html').read_text())

    def test_without_a_style_the_plain_page_and_one_stderr_line(self):
        folder, _, err = self.csv_export({'PATH': str(self.root)})
        page = (folder / '01_brief_csv-export.html').read_text()
        self.assertNotIn('data-lahe-doc-style', page)
        self.assertNotIn('class="hero"', page)
        self.assertIn('.callout-req', page)
        self.assertIn('<nav aria-label="Dossier">', page)
        self.assertEqual(len(err.strip().splitlines()), 1)
        self.assertIn('House style not found', err)
        self.assertIn('FORGE_DOC_STYLE_DIR', err)
        self.assertIn('lahe', err)
        self.assertFalse((folder / '.lahe-fonts').exists())

    def test_an_unusable_variable_falls_back_and_says_why(self):
        empty = self.root / 'empty'
        empty.mkdir()
        folder, _, err = self.csv_export({'PATH': str(self.root), 'FORGE_DOC_STYLE_DIR': str(empty)})
        self.assertNotIn('data-lahe-doc-style', (folder / '01_brief_csv-export.html').read_text())
        self.assertEqual(len(err.strip().splitlines()), 1)
        self.assertIn('FORGE_DOC_STYLE_DIR is not usable', err)
        self.assertIn('system-tokens.css is missing', err)

    def test_a_style_missing_a_component_is_refused(self):
        thin = self.root / 'thin'
        shutil.copytree(STYLE_FIXTURE, thin)
        (thin / 'document.css').write_text('body { color: black; } :root { --surface: white; }')
        _, _, err = self.csv_export({'PATH': str(self.root), 'FORGE_DOC_STYLE_DIR': str(thin)})
        self.assertIn('has no .toplinks', err)

    def test_command_line_builds_styled_pages_and_falls_back(self):
        script = ROOT / 'skills/feature-forge/scripts/build_feature_docs.py'
        folder = self.root / 'cli'
        shutil.copytree(ROOT / 'tests/fixtures/csv-export', folder)
        run = lambda env: subprocess.run([sys.executable, str(script), str(folder)],
                                         env=env, capture_output=True, text=True)
        styled = run(dict(os.environ, **WITH_STYLE))
        self.assertEqual(styled.returncode, 0, styled.stderr)
        self.assertEqual(styled.stderr, '')
        self.assertIn('data-lahe-doc-style', (folder / '01_brief_csv-export.html').read_text())
        bare = self.root / 'bare-path'
        bare.mkdir()
        (bare / 'pandoc').symlink_to(shutil.which('pandoc'))
        env = {key: value for key, value in os.environ.items() if key != 'FORGE_DOC_STYLE_DIR'}
        env['PATH'] = str(bare)
        plain = run(env)
        self.assertEqual(plain.returncode, 0, plain.stderr)
        self.assertEqual(len(plain.stderr.strip().splitlines()), 1)
        self.assertIn('House style not found', plain.stderr)
        self.assertNotIn('data-lahe-doc-style', (folder / '01_brief_csv-export.html').read_text())


    def make_command(self, name, content, mode=0o755):
        """A fake lahe command in its own folder on PATH; returns the folder."""
        bindir = self.root / ('bin-' + name)
        bindir.mkdir()
        command = bindir / 'lahe'
        (command.write_bytes if isinstance(content, bytes) else command.write_text)(content)
        command.chmod(mode)
        return bindir

    def test_an_unusable_variable_with_working_lahe_uses_lahe_and_says_so(self):
        clone = self.make_lahe_clone('wrapper')
        empty = self.root / 'empty'
        empty.mkdir()
        folder = self.root / 'csv-export'
        shutil.copytree(ROOT / 'tests/fixtures/csv-export', folder)
        _, err = self.build(folder, {'PATH': str(clone['bin']), 'FORGE_DOC_STYLE_DIR': str(empty)})
        self.assertIn('FIXTURE-STYLE-TOKENS', (folder / '01_brief_csv-export.html').read_text())
        self.assertEqual(len(err.strip().splitlines()), 1)
        self.assertIn('FORGE_DOC_STYLE_DIR is not usable', err)
        self.assertIn(str(empty), err)
        self.assertIn('system-tokens.css is missing', err)
        self.assertIn('Lahe', err)

    def assert_lahe_found_but_not_located(self, content):
        bindir = self.make_command('odd', content)
        folder = self.root / 'csv-export'
        shutil.copytree(ROOT / 'tests/fixtures/csv-export', folder)
        _, err = self.build(folder, {'PATH': str(bindir)})
        self.assertNotIn('data-lahe-doc-style', (folder / '01_brief_csv-export.html').read_text())
        self.assertEqual(len(err.strip().splitlines()), 1)
        self.assertIn('found lahe at ' + str(bindir / 'lahe'), err)
        self.assertIn('could not locate its style folder', err)
        self.assertIn('FORGE_DOC_STYLE_DIR', err)
        self.assertNotIn('Install Lahe', err)
        self.assertEqual(err.count('House style not found'), 1)

    def test_an_empty_lahe_command_names_itself_and_asks_for_the_variable(self):
        self.assert_lahe_found_but_not_located('')

    def test_a_binary_lahe_command_names_itself_and_asks_for_the_variable(self):
        self.assert_lahe_found_but_not_located(b'\x7fELF\x02\x01\x01\x00\xff\xfe\x00\x80' * 20)

    def test_a_wrapper_with_a_relative_path_is_not_guessed_at(self):
        self.assert_lahe_found_but_not_located('#!/bin/sh\nexec node ../clone/bin/lahe.js "$@"\n')

    def test_a_callout_that_opens_with_a_heading_keeps_it_inside_the_panel(self):
        folder = self.root / 'heading'
        folder.mkdir()
        (folder / '01_page.md').write_text(
            '# Page\n\nLede.\n\n## Part\n\n::: callout-question\n### Why this\n\nBecause.\n:::\n')
        self.build(folder, WITH_STYLE)
        page = (folder / '01_page.html').read_text()
        panel = re.search(r'<div[^>]*insight insight--caveat[^>]*>(.*?)</div>', page, re.S)
        self.assertIsNotNone(panel, 'the callout did not become an insight panel')
        self.assertIn('Why this', panel.group(1))
        self.assertIn('Because.', panel.group(1))
        self.assertNotIn('<section class="callout', page)


class LayoutTest(unittest.TestCase):
    """The HTML rewrites in doc_layout, on small inputs and without Pandoc."""

    def test_a_run_of_same_kind_callouts_merges_into_one_panel(self):
        html = ('<div class="callout callout-metric"><p>One</p></div>\n'
                '<div class="callout callout-metric"><p>Two</p></div>\n'
                '<p>Between</p>\n'
                '<div class="callout callout-metric"><p>Three</p></div>')
        out = layout.merge_callout_runs(layout.map_callouts(html))
        self.assertEqual(out.count('<div'), 2)
        self.assertEqual(out.count('class="insight callout-metric"'), 2)
        first = out[:out.index('<p>Between</p>')]
        self.assertIn('One', first)
        self.assertIn('Two', first)
        self.assertEqual(first.count('<div'), 1)
        self.assertIn('Three', out[out.index('<p>Between</p>'):])

    def test_a_different_kind_or_label_ends_the_run(self):
        html = ('<div class="callout callout-metric"><p>One</p></div>'
                '<div class="callout callout-suggest"><p>Two</p></div>')
        out = layout.merge_callout_runs(layout.map_callouts(html))
        self.assertEqual(out.count('<div'), 2)

    def test_merging_keeps_the_ids_of_merged_callouts_as_anchors(self):
        html = ('<div id="a" class="callout callout-metric"><p>One</p></div>'
                '<div id="b" class="callout callout-metric"><p>Two</p></div>')
        out = layout.merge_callout_runs(layout.map_callouts(html))
        self.assertIn('<span id="b"></span>', out)

    def test_requirement_callouts_lose_their_wrapper_and_keep_a_label(self):
        html = ('<div id="r1" class="callout-req"><p>R1: must work</p></div>\n'
                '<div class="callout-metric"><p>Kept</p></div>')
        out = layout.unwrap_plain_callouts(layout.map_callouts(html))
        self.assertNotIn('callout-req', out)
        self.assertIn('<p class="eyebrow" id="r1">Requirement</p>', out)
        self.assertIn('<p>R1: must work</p>', out)
        self.assertEqual(out.count('<div'), 1)
        self.assertIn('insight', out)

    def test_a_section_callout_becomes_a_div_with_its_heading_inside(self):
        html = ('<section id="q" class="callout-question"><h3>Heading</h3>'
                '<section><p>Nested</p></section><p>Body</p></section><p>After</p>')
        out = layout.callout_sections_to_divs(html)
        self.assertEqual(out, '<div id="q" class="callout-question"><h3>Heading</h3>'
                              '<section><p>Nested</p></section><p>Body</p></div><p>After</p>')
        self.assertIn('insight insight--caveat', layout.map_callouts(out))


class PortabilityTest(unittest.TestCase):
    def test_skills_name_no_machine_paths(self):
        for source in (ROOT / 'skills').rglob('*'):
            if source.is_file() and source.suffix in ('.py', '.md', '.html'):
                text = source.read_text(encoding='utf-8', errors='replace')
                self.assertIsNone(re.search(r'/Users/|/home/', text), str(source))


if __name__ == '__main__':
    unittest.main()
