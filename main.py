#!/usr/bin/env python3
"""Write the developer's production excuse to /output/entry.txt.

The entry is one funny single line: the excuse a developer gives when
code breaks in production. The grader wants UTF-8 text of 1-200
characters, a single non-blank line, so this script checks those three
properties before writing anything.
"""

import os

EXCUSE = (
    "The hotfix I pushed to fix production is now the reason production "
    "is down. On the bright side, the deployment itself worked perfectly."
)


def check(line):
    if not line.strip():
        raise SystemExit("excuse is blank")
    if len(line) > 200:
        raise SystemExit(
            f"excuse is {len(line)} chars, over the 200 limit"
        )
    if "\n" in line:
        raise SystemExit("excuse must be one line")


def main():
    check(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
