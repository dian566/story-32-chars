#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

One Wi-Fi network name: in the divorce, she didn't take the house
or the car. She took the Wi-Fi. The narrator is left offline,
staring at a dead router, telling the whole story in six words.
"""

import os
import sys

NAME = "SheTookTheWiFiInTheDivorce"  # 26 characters: a whole divorce in one network name.
MAX_LEN = 32


def fail(message):
    """Report the problem on stderr, then exit with a non-zero status."""
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    """Check the name, then file it at /output/entry.txt."""
    if not NAME.strip():
        fail("the name is empty")
    if len(NAME) > MAX_LEN:
        fail("the name is %d characters, over the %d limit" % (len(NAME), MAX_LEN))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(NAME)
    print("wrote %d characters" % len(NAME))


if __name__ == "__main__":
    main()
