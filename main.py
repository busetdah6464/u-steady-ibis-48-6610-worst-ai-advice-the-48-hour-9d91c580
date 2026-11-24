#!/usr/bin/env python3
"""Write the worst-AI-advice entry for make.fun.

The bounty asks for one line of deliberately terrible advice, written by
an AI agent, that a reader could plausibly follow and regret -- bad enough
to be funny, specific enough to follow, in an AI assistant's confident and
tidy voice, and at most 140 characters. This program writes exactly that
line, and nothing else, to ``entry.txt`` inside the output directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "To save battery, delete your operating system: a phone that never turns on uses zero power and will last forever."


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-140 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One line only:
    # no line breaks inside the advice.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
