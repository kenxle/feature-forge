#!/usr/bin/env python3
"""Record legacy/current skill sources and probe the bundled dossier renderer."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[4]

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True)

def describe(label, path, content):
    return {'baseline': label, 'path': path,
            'sha256': hashlib.sha256(content.encode()).hexdigest(),
            'headings': re.findall(r'^#{1,6} .+$', content, re.M)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--legacy-root', type=Path, required=True)
    parser.add_argument('--before', default='5a450e5^')
    parser.add_argument('--current', default='93c35d1')
    args = parser.parse_args()
    output = Path(__file__).resolve().parent
    sources = []
    for ref, label in ((args.before, 'pre-runbook-package'), (args.current, 'current-package')):
        paths = git('ls-tree', '-r', '--name-only', ref, 'skills').splitlines()
        for path in paths:
            if path.endswith(('.md', '.py', '.html')) and '/vendor/' not in path:
                sources.append(describe(label, path, git('show', ref + ':' + path)))
    for host in ('.claude', '.codex'):
        base = args.legacy_root / 'previous' / host
        for path in sorted(base.rglob('*')):
            if path.is_file() and path.suffix in {'.md', '.py', '.html'} and '__pycache__' not in path.parts:
                text = path.read_text()
                sources.append(describe('pre-update-installed-' + host[1:], str(path.relative_to(base)), text))
    manifest = {'before_revision': git('rev-parse', args.before).strip(),
                'current_revision': git('rev-parse', args.current).strip(), 'sources': sources}
    (output / 'sources.json').write_text(json.dumps(manifest, indent=2) + '\n')

    inventory = json.loads((output / 'inventory.json').read_text())
    excerpts = ['# Legacy source excerpts', '',
                'Exact excerpts from the preserved pre-update installed skills. The source manifest records file fingerprints. These excerpts are evidence for the audit, not active skill instructions.', '']
    for item in inventory:
        legacy = args.legacy_root / 'previous/.claude' / item['legacy_file']
        assert item['legacy_excerpt'] in legacy.read_text(), 'Excerpt not found: ' + item['id']
        excerpts.extend(['## ' + item['id'], '', item['title'], '',
                         'Source: `' + item['legacy_file'] + '`. Category: ' + item['category'] + '.', ''])
        excerpts.extend('> ' + line for line in item['legacy_excerpt'].splitlines())
        excerpts.extend(['', 'Current gap: ' + item['finding'], '',
                         'History: ' + item['history'], ''])
    (output / 'legacy-excerpts.md').write_text('\n'.join(excerpts))

    fixture_root = Path(tempfile.mkdtemp(prefix='forge-audit-render-'))
    renderer = fixture_root / 'skills/feature-forge/scripts/build_feature_docs.py'
    renderer.parent.mkdir(parents=True)
    renderer.write_text(git('show', args.current + ':skills/feature-forge/scripts/build_feature_docs.py'))
    header = fixture_root / 'skills/feature-forge/assets/header.html'
    header.parent.mkdir(parents=True)
    header.write_text(git('show', args.current + ':skills/feature-forge/assets/header.html'))
    spec = importlib.util.spec_from_file_location('forge_renderer', renderer)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    folder = fixture_root / 'probe'
    folder.mkdir()
    (folder / '01_brief_probe.md').write_text('''# Compatibility probe

Inspect an existing document convention without changing its source.

## Question

<div class="insight insight--caveat" data-label="Open question"><p>Does this keep its house styling?</p></div>

## Flow

```mermaid
flowchart TD
  Request --> Result
```
''')
    rendered = module.build(folder)
    page = rendered[0].read_text()
    probe = {'source_unchanged': '```mermaid' in (folder / '01_brief_probe.md').read_text(),
             'house_markup_preserved': 'class="insight insight--caveat"' in page,
             'house_component_css_bundled': bool(re.search(r'\.insight\b', page)),
             'mermaid_remains_code': 'class="mermaid"' in page or 'class="language-mermaid"' in page,
             'diagram_svg_present': '<svg' in page,
             'browser_scripts_present': '<script' in page,
             'dossier_navigation_present': 'aria-label="Dossier"' in page}
    (output / 'renderer-probe.json').write_text(json.dumps(probe, indent=2) + '\n')
    print(json.dumps({'source_manifest': 'sources.json', 'inventory_excerpts': 'verified', 'probe': probe}))

if __name__ == '__main__':
    main()
