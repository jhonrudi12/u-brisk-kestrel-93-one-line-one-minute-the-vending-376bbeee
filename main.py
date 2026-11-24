#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Reads the single pickup line shipped in entry.txt next to this file,
checks it against the contest gate (one line, 1-200 UTF-8 characters,
more than whitespace), and writes it unchanged to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Standard library only. Deterministic, no network, no randomness, and
no writes outside the output directory.
"""

import os
import sys
from pathlib import Path

LIMIT = 200


def load_line() -> str:
    path = Path(__file__).resolve().parent / "entry.txt"
    text = path.read_text(encoding="utf-8")
    # Strip one trailing line ending, CRLF or LF, so the output is exactly
    # the line itself and nothing else.
    if text.endswith("\r\n"):
        text = text[:-2]
    elif text.endswith("\n"):
        text = text[:-1]
    return text


def main() -> int:
    line = load_line()
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not line.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if len(line) > LIMIT:
        print(f"entry is {len(line)} characters, limit is {LIMIT}", file=sys.stderr)
        return 1
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(line, encoding="utf-8")
    print(f"wrote {len(line)}-character entry to {out / 'entry.txt'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
