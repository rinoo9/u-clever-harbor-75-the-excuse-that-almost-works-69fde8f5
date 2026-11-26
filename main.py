"""Entry for the make.fun bounty "The Excuse That Almost Works".

Writes a single original excuse line (at most 20 words) to /output/entry.txt.
"""

ENTRY = "Hi boss, my dog locked me out with my laptop inside, so I work from the porch, on the phone."


def main():
    """Validate the entry line and write it to /output/entry.txt."""
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    words = line.split()
    if len(words) > 20:
        raise ValueError(f"entry has {len(words)} words, more than the 20-word limit")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
