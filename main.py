#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Deterministic, no network, no randomness, no clock.
"""

import os

TEXT = (
    "You have read a thousand texts today. This one asks nothing of you. "
    "Somewhere a tide comes in over flat sand, slow as sleep, writing one "
    "line and erasing it, writing one line and erasing it. Nothing is kept. "
    "Nothing is lost. Stay a while — the sea has nowhere else to be."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
