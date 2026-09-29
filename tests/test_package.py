import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

installer = module('installer', ROOT / 'scripts/install.py')
renderer = module('renderer', ROOT / 'skills/feature-forge/scripts/build_feature_docs.py')
support = module('support', ROOT / 'skills/feature-forge/scripts/forge_support.py')

class PackageTest(unittest.TestCase):
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
            shutil.copytree(ROOT / 'examples/csv-export', root)
            pages = renderer.build(root)
            brief = (root / '01_brief_csv-export.html').read_text()
            self.assertIn('CSV quoting', brief)
            self.assertIn('Review history', brief)
            self.assertIn('03_plan_csv-export.html', brief)
            self.assertNotIn('forge-include:', brief)
            self.assertNotIn('<script', brief)
            self.assertEqual(len(pages), 4)

if __name__ == '__main__':
    unittest.main()
