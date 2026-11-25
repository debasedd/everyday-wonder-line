#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line — writes one line to /output/entry.txt.

The line is a single sentence about a small moment of wonder in everyday
life: the lift doors open on a stranger humming my dead grandfather's
favourite song, and for one floor the whole building feels like his
kitchen again. The surprise is in the phrasing itself — an ordinary lift
ride turning, for one floor, into a dead man's kitchen — grounded in
something real and specific: a stranger's hum, a song, one floor.
"""

import os

LINE = "The lift doors opened on a stranger humming my dead grandfather's favourite song, and for one floor the whole building felt like his kitchen again."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
