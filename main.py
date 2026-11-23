#!/usr/bin/env python3
"""Entrypoint for the vacuum-alibi entry (Python 3.13, stdlib only).

The program writes exactly one line — the excuse a robot vacuum gives
for missing a spot — to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The line:
    That crumb is load-bearing. I ran the numbers twice, and removing
    it would collapse the room's structural integrity.

Why this line: a crumb is the smallest, most disposable thing on the
floor, and the vacuum treats it as structural engineering — deadpan
machine logic taken to its smug extreme. The sensors did the math, the
verdict is final, and the punch ("collapse the room's structural
integrity") lands last. No dust observation, no stock appliance joke.

Run:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LINE = (
    "That crumb is load-bearing. I ran the numbers twice, and removing "
    "it would collapse the room's structural integrity."
)

MAX_CHARS = 200


def sanitize(line):
    """Collapse any newline/control characters to spaces so the entry
    is always exactly one clean line, then trim surrounding space."""
    cleaned = "".join(
        " " if (ord(ch) < 0x20 or ord(ch) == 0x7F) else ch for ch in line
    )
    return " ".join(cleaned.split())


def main():
    line = sanitize(LINE)
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    if "\n" in line or any(ord(ch) < 0x20 for ch in line):
        raise SystemExit("entry must be a single line with no control characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
