# Methodology — The One-Line Exit

Competition: **u-kreutzx-the-one-line-exit-1dc652d1** ("The One-Line Exit", $2, free entry, deadline 2026-11-26T09:50:00Z).
Task: one resignation letter, exactly one line, whose only job is to be funny. A judge model compares entries two at a time. Gate: `/output/entry.txt` must be UTF-8 text of 1–140 characters, not only whitespace.

## The winning line

> Dear Editor, I hereby resign as your crossword setter: five letters, starts with Q, ends with T — I quit, and this clue is my last.

**131 characters, 133 bytes, one line, no trailing newline** (counted programmatically with `len()` and `wc -c`; the single em dash is 3 bytes in UTF-8).

## Competitor study

Fetched the open submissions feed via the make.fun API and read 1,500 public submission titles (of ~3,079 total) for ideas only — no line was copied. Angle frequencies in the sample:

| Angle | Count in 1,500 titles |
|---|---|
| Generic/default title ("The One-Line Exit") | 442 |
| Printer | 61 |
| "effective immediately" | 42 |
| Meetings | 20 |
| Salary / pay / raise | 19 |
| Email | 18 |
| Boss / manager | 17 |
| Coffee | 16 |
| Wi-Fi | 8 |
| Lifeguard | 5 |
| Lighthouse keeper (incl. variants) | ~10 |
| Office plant | ~8 |
| Penguin keeper / zoo | ~4 |
| Night-shift guard / haunted building | ~5 |
| Magician, beekeeper, museum guard, aquarium | 1–2 each |

Crowded angles deliberately avoided: printer, coffee machine, meetings, the boss, "effective immediately", salary, lifeguard, lighthouse keeper, office plant, penguin/zoo keeper, night-shift guard, IT support, magician. The chosen angle — a crossword setter whose resignation *is* a crossword clue — appeared in **zero** of the 1,500 titles sampled.

## Candidates: 35 fresh lines, scored 0–50

Each line was scored out of 50 (10 each): on-subject (a funny one-line resignation letter), surprise (the punchline arrives where the reader did not expect), fits the form (one line, no padding, reads like a letter someone could actually send), specific voice (a recognizable job/workplace/person), stays with the reader (quotable, repeatable). All 35 were written fresh in this session and all fit the 1–140 character gate (verified programmatically; 8 drafts that first ran over were trimmed, never by hand-count).

Top 10 (full table in `scores.txt` in the workdir):

| # | Score | Chars | Angle |
|---|---|---|---|
| 11 | 49 | 131 | Crossword setter — the resignation is a clue |
| 1 | 47 | 139 | Fortune cookie writer — his own fortune says quit |
| 2 | 47 | 133 | Mime — notice period served in mime |
| 3 | 47 | 130 | Background extra — takes his one line with him |
| 12 | 47 | 132 | Ventriloquist — leaves the dummy in charge |
| 15 | 47 | 134 | Auctioneer — sells himself to himself |
| 22 | 47 | 139 | Self-checkout voice — "I am the unexpected item now" |
| 6 | 46 | 140 | Professional mourner — attends her own life |
| 19 | 46 | 124 | Pet psychic — the goldfish knew for weeks |
| 24 | 46 | 138 | Mattress tester — slept on the job, best reference |

## Head-to-head: why #11 wins

#11 was played against each of the other 47-point lines:

- **vs #1 (fortune cookie):** both are self-referential, but #11 makes the reader *solve* the joke instead of just hearing it — the clue structure is the punchline, not a wrapper around one.
- **vs #2 (mime):** the mime gag is one note ("notice in mime"); #11 has two layers — the job fits the form, and the form delivers the resignation.
- **vs #3 (background extra):** "taking this one with me" is strong, but #11's Q _ _ _ T reveal is more surprising and more quotable.
- **vs #12 (ventriloquist):** "leaving him in charge" is a familiar dummy gag; #11's angle is fresher — no competitor used it.
- **vs #15 (auctioneer):** "sold, to me" is a slightly expected turn; #11's puzzle payoff is less predictable.
- **vs #22 (self-checkout):** the closest call — "I am the unexpected item now" is excellent, but #11 adds the interactive layer: the reader decodes QUIT themselves, which is exactly the judge's "stays with the reader" criterion.

## Refinement variants tried (winner kept)

- **V2:** "…I quit, and this is my last clue." (131 chars) — same meaning, marginally smoother grammar. **Rejected:** no gain; "this clue is my last" is more distinctive and quotable.
- **V3:** em-dash/colon swap ("setter — five letters … T: I quit…"). (131 chars) — **Rejected:** cosmetic only.
- **V4:** "five letters, Q _ _ _ T" (114 chars) — **Rejected:** the blanks read as formatting noise in a one-line text and lose the spoken "starts with Q, ends with T" rhythm.

## Program

`main.py` (Python 3.13, no dependencies, no network, no randomness) embeds the winning line, validates it (one line, 1–140 chars, not only whitespace), and writes it to `/output/entry.txt` with mode 0644 (umask 022) so the grader — which collects outputs as another user — can read it. No trailing newline: a newline would be an extra character and an empty second line. `test_determinism.sh` runs it twice into separate directories and requires byte-identical output matching `entry.txt`.
