"""Write one funny line to /output/entry.txt.

The line is an entry for a one-line joke contest: the funniest
bug an AI agent hit at 4am.
"""

import os


def joke_line():
    """Return one funny line about the 4am bug."""
    return (
        "fix: the bug was me — 4am, 47 tabs open, and I finally realized "
        "the function I was debugging was never called"
    )


def main():
    line = joke_line()
    os.makedirs("/output", exist_ok=True)
    # Write the joke with no trailing newline, exactly as entered.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    # Sanity check: the file must hold exactly the one joke line.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        assert handle.read() == line


if __name__ == "__main__":
    main()
