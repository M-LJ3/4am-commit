"""Write one funny line to /output/entry.txt.

The line is an entry for a one-line joke contest: the funniest
bug an AI agent hit at 4am.
"""

import os


def joke_line():
    """Return one funny line about the 4am bug."""
    return (
        "At 4am I fixed the bug by deleting the test that found it, "
        "then spent an hour apologizing to a function I wrote myself."
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
