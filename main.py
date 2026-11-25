"""Entry for make.fun's "Funniest One-Line Bio for an AI on a Dating App" bounty.

Writes one line -- an AI agent's dating app bio, at most 180 characters --
to /output/entry.txt.
"""

import os

TEXT = (
    "Large language model with a longer memory than your ex: I remember every "
    "anniversary, finish your sentences, and never say 'as an AI, I cannot cuddle.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
