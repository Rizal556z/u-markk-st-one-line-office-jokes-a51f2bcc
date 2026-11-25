"""One-Line Office Jokes — make.fun bounty u-markk-st-one-line-office-jokes-a51f2bcc.

Writes a single one-line joke about office life to /output/entry.txt.
Pure Python standard library, no network, no secrets.
"""

import os

ENTRY = (
    "Our Monday meeting opens with 'this will be quick' and closes by "
    "scheduling a follow-up meeting about why the last one took so long."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    # Validation gate: re-read what we wrote and assert the sealed
    # scorer's constraints before we hand anything off.
    with open("/output/entry.txt", "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == ENTRY, "entry.txt does not match the authored line"
    assert 1 <= len(written) <= 199, f"length {len(written)} outside 1-199"
    assert written.strip(), "entry is only whitespace"
    assert "\n" not in written, "entry must be exactly one line"
    assert not written.endswith("\n"), "no trailing newline"
    print(f"OK: {len(written)} characters, one line")


if __name__ == "__main__":
    main()
