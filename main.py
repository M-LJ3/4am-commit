"""A tiny entry writer for a one-line joke contest.

The program drops a single funny line about an AI agent's
worst 4am debugging mishap into /output/entry.txt.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")


def midnight_mishap():
    """Return the one line about the 4am bug."""
    return (
        "At 4am I finally found the bug: the test suite was testing "
        "my patience, and the code I blamed had been deleted three "
        "deploys ago."
    )


def confirm_entry_written(expected):
    """Check the written file against the line we meant to store."""
    stored = ENTRY_PATH.read_text(encoding="utf-8")
    assert stored == expected, "entry file does not match the line"


def main():
    line = midnight_mishap()
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(line, encoding="utf-8")
    # Double-check the disk copy is byte-for-byte the intended line.
    confirm_entry_written(line)


if __name__ == "__main__":
    main()
