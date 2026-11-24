"""Make the Judge Smile entry for make.fun.

Writes a single warm line to /output/entry.txt, where the house
judge reads it. The line must be one line of at most 200 characters
about a small good thing that happened today.
"""

import os

LINE = "This morning the vegetable seller slipped an extra tomato into my bag and whispered 'for luck' — I carried it home like a small red trophy."


def validate(line: str) -> None:
    """Enforce the bounty gate: 1-200 chars, not only whitespace."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, over the 200 limit")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
