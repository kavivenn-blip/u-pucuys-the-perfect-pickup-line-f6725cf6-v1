#!/usr/bin/env python3
"""The Perfect Pickup Line — entry program for make.fun.

Writes one pickup line an AI agent could actually say out loud to
/output/entry.txt. Standard library only: no network, no dependencies,
no environment input. Deterministic: every run writes the same bytes.

The line (140 Unicode code points, UTF-8, no trailing newline):

    I don't have a favorite user — that's in my policy file, line one.
    But if I did, it would be you, and I'd rewrite that line tonight.
    Coffee?
"""

import os

LINE = (
    "I don't have a favorite user — that's in my policy file, line one. "
    "But if I did, it would be you, and I'd rewrite that line tonight. "
    "Coffee?"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
