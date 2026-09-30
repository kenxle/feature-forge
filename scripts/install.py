#!/usr/bin/env python3
"""Install project-local skills, refusing existing destinations."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('feature-forge', 'brief', 'architecture', 'plan', 'whetstone')

def install(project, dry_run=False):
    project = Path(project).resolve()
    if not project.is_dir():
        raise ValueError('Project must be an existing directory')
    base = project / '.claude' / 'skills'
    if any(p.is_symlink() for p in (project / '.claude', base)):
        raise ValueError('Refusing symlinked install directories')
    conflicts = [str(base / name) for name in NAMES
                 if (base / name).exists() or (base / name).is_symlink()]
    if conflicts:
        raise ValueError('Existing destinations; nothing copied: ' + ', '.join(conflicts))
    for name in NAMES:
        print(('Would install ' if dry_run else 'Installing ') + str(base / name))
    if dry_run:
        return
    base.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for name in NAMES:
            target = base / name
            target.mkdir()  # Exclusive creation also handles a concurrent installer.
            created.append(target)
            shutil.copytree(ROOT / 'skills' / name, target, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    except Exception:
        for target in reversed(created):
            shutil.rmtree(target)  # Only this invocation's newly created directories.
        raise

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        install(args.project, args.dry_run)
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc) + '\n')

if __name__ == '__main__':
    main()
