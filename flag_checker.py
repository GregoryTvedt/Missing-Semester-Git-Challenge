#!/usr/bin/env python3
"""Check a text file of flag guesses (one per line) against known SHA-256 hashes."""

import hashlib
import sys

TARGET_HASHES = [
    "a545fb5419670bc854a0b55328c768b5fceba63a9886da24da4a0c19164c3202",
    "7eb40442428abaebd7e07ce2eb9b982b13bb4f092a9907719ad51bd9c97b6643",
    "f1fe2f4ec671c86a90822edc81c1c3f2c980511149fd7e489cc089ead73d79e3",
    "45bc7ed0034cd3cefe7b5792bc1ee27594922bc245e80d7c2271cab68e3b0139",
    "89faa03e2c1370eaedc211aedffd8c3b1237e68d846e33adb6ae1cb7924b562e",
    "973a240760c68ad6b64a17397d98ce724e9c229f7c5744a34580326f1a51011c",
]


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <flags.txt>")
        return 1

    path = sys.argv[1]
    try:
        with open(path, "r", encoding="utf-8") as f:
            # Strip newline/whitespace; skip blank lines
            guesses = [line.strip() for line in f if line.strip()]
    except OSError as e:
        print(f"Error reading {path}: {e}")
        return 1

    targets = set(h.lower() for h in TARGET_HASHES)
    found = {}  # hash -> flag

    for guess in guesses:
        digest = sha256_hex(guess)
        if digest in targets and digest not in found:
            found[digest] = guess

    print(f"Checked {len(guesses)} guess(es) against {len(targets)} hash(es).\n")

    if found:
        print("Correct flags:")
        for digest, flag in found.items():
            print(f"  [+] {flag}  ({digest[:12]}...)")
    else:
        print("No correct flags found.")

    remaining = [h for h in TARGET_HASHES if h.lower() not in found]
    print(f"\nScore: {len(found)}/{len(targets)}")
    if remaining:
        print(f"Still unsolved: {len(remaining)}")
        for h in remaining:
            print(f"  [ ] {h[:12]}...")
    else:
        print("All flags found!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
