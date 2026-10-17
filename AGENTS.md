# Working in this repository

This repo is the source of the Feature Forge skills package. It holds the skills and the tools that ship with them. It is not a project that uses them. Read [README.md](README.md) for what the process does.

## Layout

- `skills/`: the five skills that get installed: `feature-forge`, `brief`, `architecture`, `plan` and `whetstone`. Each has a `SKILL.md`. The `feature-forge` skill also carries `references/`, `scripts/` (the dossier renderer) and `assets/`.
- `scripts/install.py`: copies the skills into a project's `.claude/skills/`. It refuses to overwrite existing copies.
- `tests/`: the package tests. `tests/fixtures/csv-export/` is a sample feature folder used to test the renderer. It is test data, not a real feature.
- `docs/`: notes on LAHE pairing, verification and research credits, plus `BOARD.md`, the backlog.

## Installed copies do not update from here

The installer copies files. A skill running from a project's `.claude/skills/` or from `~/.claude/skills/` is a separate copy, and it does not change when this repo changes.

- When someone reports a problem with a skill, find out which copy they ran. Compare it with this repo before editing: `diff -rq skills/<name> <installed path>/<name>`.
- Fix the problem here first, so everyone who installs the package gets the fix. Then reinstall or update the copy that broke.
- Say which copy you changed. Do not copy files between an installed copy and this repo without checking what the other side has. An installed copy can hold local changes that do not belong in the public package.

## Rules for the skills

- **Keep the package portable.** Nothing in this repo may name a person's machine, home folder, private repo or private tool. That includes skill text, examples, tests and commit messages.
- **Write skill text plainly.** Use one idea per sentence and common words. Spell out what the agent should do and who does it. Agents follow plain instructions more reliably than compressed ones.
- **Links between skills are relative.** The `feature-forge` skill's references are linked from the sibling skills as `../feature-forge/references/...`. A test checks that every local Markdown link resolves.

## Checks

Run from the repo root:

```sh
python3 -m unittest discover -s tests -v
```

Run it after changing anything in `skills/`, `scripts/` or `tests/`. Pandoc tests skip when Pandoc is not installed. Say so if they skipped.

Before pushing, scan for private references:

```sh
git grep -nE '/Users/|/home/|~/\.claude|\.local\.md'
```

Every hit should be a deliberate generic example, such as the `~/.claude/skills/` mention above.

## Commits

- Keep commits small and focused. Separate wording changes from behavior changes.
- `*.local.md` files are local working notes. They are excluded from git and are not part of the package.
