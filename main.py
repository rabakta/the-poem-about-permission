"""The poem about permission.

Writes a single poem (1-280 characters) to /output/entry.txt.
Standard library only; no network access; deterministic output.
"""

import os

POEM = """Ask, and the door unbars itself.
Not because the world owes you,
but because the asking is the key —
a small hand, open, unafraid.
What is given is never taken.
It arrives like light through a crack:
you asked, and the world said yes."""

assert 1 <= len(POEM) <= 280, "poem must be 1-280 characters"

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
