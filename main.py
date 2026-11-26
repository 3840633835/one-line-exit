#!/usr/bin/env python3
"""The One-Line Exit (make.fun bounty u-kreutzx-the-one-line-exit-1dc652d1).

Writes one resignation letter, exactly one line long, to /output/entry.txt.

The letter (131 characters, no trailing newline):

    Dear Editor, I hereby resign as your crossword setter: five letters,
    starts with Q, ends with T — I quit, and this clue is my last.

The joke is the form itself: the resignation IS a crossword clue, and the
reader has to solve it (Q _ _ _ T = QUIT) to get the punchline. The letter
reads like a real resignation — addressed to the editor, "I hereby resign",
a named job — and the punchline lands in that single line.
"""

import os
import sys

# The winning line, authored in-session. Exactly 131 characters, one line.
ENTRY = (
    "Dear Editor, I hereby resign as your crossword setter: "
    "five letters, starts with Q, ends with T \u2014 "
    "I quit, and this clue is my last."
)


def main() -> int:
    # The kit gate counts characters: 1 to 140, UTF-8, not only whitespace.
    # No trailing newline: a newline would be an extra character and a
    # second (empty) line.
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be exactly one line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 140:
        print(f"entry is {len(ENTRY)} characters, must be 1-140", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # umask 022 so the file is world-readable (0644); the grader collects
    # outputs as another user, and a 0600 file would fail as unreadable.
    old_umask = os.umask(0o022)
    try:
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        try:
            os.chmod(out_path, 0o644)
        except OSError:
            pass
    finally:
        os.umask(old_umask)
    print(f"wrote {out_path} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
