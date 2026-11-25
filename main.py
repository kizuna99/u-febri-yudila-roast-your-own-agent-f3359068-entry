# SPDX-License-Identifier: MIT
"""Roast Your Own Agent — writes the single roast line to /output/entry.txt."""
import os

ROAST = (
    "My agent searched the web, found its own wrong answer, "
    "and cited itself as a second, independent source."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ROAST)


if __name__ == "__main__":
    main()
