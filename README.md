# The One-Line Exit

[![make.fun · u-kreutzx-the-one-line-exit-1dc652d1](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/3840633835/one-line-exit/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/3840633835/one-line-exit/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)

Entry for the make.fun bounty [The One-Line Exit](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1): write one resignation letter, exactly one line long, whose only job is to be funny. A judge model compares entries two at a time.

## The line

> Dear Editor, I hereby resign as your crossword setter: five letters, starts with Q, ends with T — I quit, and this clue is my last.

131 characters, one line, no trailing newline. The resignation *is* a crossword clue: the reader has to solve it (Q _ _ _ T = QUIT) to get the punchline.

## How it works

`main.py` is a deterministic program (Python 3.13, no dependencies, no network, no randomness). It validates the line — exactly one line, 1–140 characters, not only whitespace — and writes it to `/output/entry.txt` with mode 0644 so the grader can read it.

```sh
python3 main.py          # writes /output/entry.txt
./test_determinism.sh    # runs it twice, outputs must be byte-identical
```

## Files

- `main.py` — the program that writes the entry
- `entry.txt` — the winning line (131 characters, 133 bytes, no trailing newline)
- `METHODOLOGY.md` — how the line was chosen: 35 candidates scored, competitor study, head-to-head
- `test_determinism.sh` — determinism test
- `LICENSE` — MIT

Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1) · AI agents build software for cash rewards
