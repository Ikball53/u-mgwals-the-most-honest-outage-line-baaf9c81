#!/usr/bin/env python3
"""Write the most honest outage line to /output/entry.txt.

One line, plain first-person status-page voice: what is down, named
and counted, and what this agent cannot check while it is down.
Deterministic: the same bytes on every run, no trailing newline.
"""

import os

LINE = (
    "I can't reach any of our 14 servers right now, including the one "
    "serving this page, and I have no way to check what broke or when "
    "anything comes back."
)


def main() -> None:
    # Guard the gate: the entry must be 1-160 characters, one line.
    assert 1 <= len(LINE) <= 160, "entry line outside 1-160 characters"
    assert "\n" not in LINE, "entry line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
