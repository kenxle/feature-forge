import base64
import contextlib
import io
import os
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from unittest.mock import patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'skills/feature-forge/scripts'))
import build_feature_docs as renderer


@unittest.skipUnless(shutil.which('pandoc'), 'Optional Pandoc not installed')
class DiagramTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.folder = self.root / 'feature'
        self.folder.mkdir()
        self.command = self.root / 'mmdc'
        self.command.write_text(
            '#!' + sys.executable + '\n'
            'from pathlib import Path\nimport sys\n'
            'source = Path(sys.argv[sys.argv.index("-i") + 1]).read_text()\n'
            'if "INVALID" in source: raise SystemExit(3)\n'
            'Path(sys.argv[sys.argv.index("-o") + 1]).write_text(\n'
            ' \'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 80">'
            '<title>Release flow</title><desc>Build then verify</desc>'
            '<text>Build</text><path d="M1 1L10 10"/></svg>\')\n')
        self.command.chmod(0o755)

    def build(self, env):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return renderer.build(self.folder, env)

    def test_diagrams_in_main_include_and_reviews_render_in_both_styles(self):
        source = '# Release\n\nLede.\n\n## Flow\n\n```mermaid\nflowchart TD\n A --> B\n```\n'
        (self.folder / '01_release.md').write_text(source + '\n<!-- forge-include: part.md -->\n')
        (self.folder / 'part.md').write_text('```mermaid\nsequenceDiagram\n A->>B: Check\n```\n')
        (self.folder / '01_release_reviews.md').write_text(source.replace('# Release', '## Review'))
        original = (self.folder / '01_release.md').read_bytes()
        styles = ({}, {'FORGE_DOC_STYLE_DIR': str(Path(__file__).parent / 'fixtures/house-style')})
        for style in styles:
            self.build(dict(style, FORGE_MERMAID_CLI=str(self.command)))
            page = (self.folder / '01_release.html').read_text()
            diagrams = re.findall(r'src="data:image/svg\+xml;base64,([^" ]+)"', page)
            self.assertEqual(len(diagrams), 3)
            for data in diagrams:
                svg = base64.b64decode(data).decode()
                self.assertIn('<text>Build</text>', svg)
                self.assertIn('<path ', svg)
            self.assertIn('alt="Build then verify"', page)
            self.assertIn('width="100" height="80" style="width:100px"', page)
            self.assertNotIn('<script', page)
            self.assertEqual((self.folder / '01_release.md').read_bytes(), original)

    def test_missing_or_failed_renderer_preserves_all_prior_pages(self):
        (self.folder / '01_good.md').write_text('# Good\n\nBody.\n')
        (self.folder / '02_diagram.md').write_text('# Diagram\n\n```mermaid\nINVALID\n```\n')
        for name in ('01_good.html', '02_diagram.html'):
            (self.folder / name).write_text('previous good output')
        for command, message in ((str(self.root / 'absent'), 'Mermaid CLI'),
                                 (str(self.command), 'diagram')):
            with self.assertRaisesRegex(ValueError, message):
                self.build({'FORGE_MERMAID_CLI': command})
            for name in ('01_good.html', '02_diagram.html'):
                self.assertEqual((self.folder / name).read_text(), 'previous good output')

    def test_no_diagram_needs_no_mermaid_installation(self):
        (self.folder / '01_doc.md').write_text('# Document\n\n```python\nprint("mermaid")\n```\n')
        self.build({'FORGE_MERMAID_CLI': str(self.root / 'absent')})
        self.assertIn('print', (self.folder / '01_doc.html').read_text())

    def test_remote_resources_and_non_svg_output_are_refused(self):
        (self.folder / '01_doc.md').write_text('# Diagram\n\n```mermaid\nflowchart TD\n A --> B\n```\n')
        for svg in ('<html>broken</html>',
                    '<svg xmlns="http://www.w3.org/2000/svg"><image href="https://example.invalid/a.png"/></svg>'):
            self.command.write_text('#!' + sys.executable + '\nfrom pathlib import Path\nimport sys\n'
                                    'Path(sys.argv[sys.argv.index("-o")+1]).write_text(' + repr(svg) + ')\n')
            with self.assertRaises(ValueError):
                self.build({'FORGE_MERMAID_CLI': str(self.command)})
