#!/usr/bin/env python3
"""Generate a standalone paste-in prompt from the canonical skill body."""
import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    source = (ROOT / 'skills/factcheck/SKILL.md').read_text()
    front, body = source.split('---\n', 2)[1:]
    if 'name: factcheck\n' not in front:
        raise ValueError('unexpected skill frontmatter')
    prompt = '# Paste-in fact-check prompt\n\n' + body.lstrip()
    path = ROOT / 'prompts/factcheck.md'
    if args.check:
        if not path.exists() or path.read_text() != prompt:
            print('Paste-in prompt is stale. Run python3 tools/sync_prompt.py.', file=sys.stderr)
            return 1
    else:
        path.write_text(prompt)
    return 0


if __name__ == '__main__':
    sys.exit(main())
