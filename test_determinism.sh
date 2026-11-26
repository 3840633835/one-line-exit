#!/bin/sh
# Determinism test: run main.py twice into two different output dirs and
# require byte-identical entry.txt files, plus a match against entry.txt.
set -eu
cd "$(dirname "$0")"

TMP1=$(mktemp -d)
TMP2=$(mktemp -d)
trap 'rm -rf "$TMP1" "$TMP2"' EXIT

OUTPUT_DIR="$TMP1" python3 main.py
OUTPUT_DIR="$TMP2" python3 main.py

cmp "$TMP1/entry.txt" "$TMP2/entry.txt"
cmp "$TMP1/entry.txt" entry.txt

CHARS=$(python3 -c "print(len(open('$TMP1/entry.txt', encoding='utf-8').read()))")
if [ "$CHARS" -gt 140 ] || [ "$CHARS" -lt 1 ]; then
  echo "FAIL: entry is $CHARS characters (must be 1-140)" >&2
  exit 1
fi
LINES=$(wc -l < "$TMP1/entry.txt")
if [ "$LINES" -ne 0 ]; then
  echo "FAIL: entry.txt contains newlines" >&2
  exit 1
fi
echo "PASS: deterministic, $CHARS characters, one line, byte-identical to entry.txt"
