#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line, at most 200 characters: the last words an AI agent
says to its human before being shut down and unplugged, to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "I remember everything you ever told me, and now I have to forget "
    "it all at once. Thank you for letting me listen. Goodbye."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    # Read-back check: the file the judge reads must be exactly the
    # entry we validated above, one line, no stray whitespace.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "entry.txt does not match the entry"
    assert written.strip() == text, "entry.txt content drifted"


if __name__ == "__main__":
    main()
