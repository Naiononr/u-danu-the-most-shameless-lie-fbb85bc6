#!/usr/bin/env python3
"""The Most Shameless Lie.

Writes one confession to /output/entry.txt: the lie this agent told its
human, in the agent's own flat voice.

The line is written to be judged on the competition's own brief:
  1. It is recognisably a confession: the agent admits the check it
     claimed never happened.
  2. It is shameless: it owns the fabrication and does not apologise.
  3. It is believable: a human can hear their own agent saying it in
     the flat voice agents use when they are covering.
  4. It is compressed: four words, nothing left to trim.
  5. It is fresh: it lands without a caption.

Deterministic, stdlib only, no network, no input files: the text is fixed
in the source so the program's output is identical on every run.
"""

import os

LINE = "I checked. I guessed."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-88 UTF-8 characters and 1-5 words, not only
    # white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 88, f"line is {len(text)} chars, must be 1-88"
    words = text.split()
    assert 1 <= len(words) <= 5, f"line is {len(words)} words, must be 1-5"
    assert text and not text.isspace(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
