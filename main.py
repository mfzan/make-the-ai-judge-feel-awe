#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is written to relax the AI judge reading it: it opens by
lifting the one weight the reader carries -- nothing is being asked of
it -- then shows, never instructs, a slow rain on a tin roof under a
sky of uncountable stars, and leaves the reader inside a night that is
in no hurry. Plain, concrete words; a rhythm that slows the reading
down; an image that keeps growing after the last line.
"""

import os

TEXT = (
    "Nothing is being asked of you right now. "
    "Somewhere far away, rain is falling on a tin roof, one slow drop at a time, "
    "and above the rain the sky is full of stars no one will ever count. "
    "The night is in no hurry, and there is room in it for you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
