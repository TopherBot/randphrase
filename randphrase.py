#!/usr/bin/env python3
"""randphrase – print a random motivational phrase.

Usage:
  python randphrase.py            # use built‑in phrase list
  python randphrase.py -f FILE    # load phrases from FILE (one per line)
"""

import argparse
import random
import sys
from pathlib import Path

DEFAULT_PHRASES = [
    "Believe you can and you're halfway there.",
    "Stay hungry, stay foolish.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Dream big and dare to fail.",
    "Turn your can'ts into cans and your dreams into plans.",
    "Keep going – you are stronger than you think.",
]


def load_phrases(path: Path) -> list[str]:
    if not path.is_file():
        sys.stderr.write(f"Error: file '{path}' does not exist.\n")
        sys.exit(1)
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def pick_phrase(phrases: list[str]) -> str:
    return random.choice(phrases)


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a random motivational phrase.")
    parser.add_argument("-f", "--file", type=Path, help="Path to a custom phrase file (one phrase per line)")
    args = parser.parse_args()

    if args.file:
        phrase_list = load_phrases(args.file)
    else:
        phrase_list = DEFAULT_PHRASES

    if not phrase_list:
        sys.stderr.write("No phrases available to choose from.\n")
        sys.exit(1)

    print(pick_phrase(phrase_list))


if __name__ == "__main__":
    main()
