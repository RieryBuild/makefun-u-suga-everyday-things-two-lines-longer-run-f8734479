"""Everyday Things, Two Lines — a toaster, explained to a 10-year-old.

Line 1 explains a toaster with one analogy: a sunbed for bread.
Line 2 says what the analogy maps (the browning, the pop-up) and
what it leaves out (the heat comes from wires, not the sun).
"""

import os

LINE1 = "A toaster is a sunbed for bread that gives each slice a quick tan, then pops it up."
LINE2 = "It maps the browning and the pop-up, but the heat comes from wires, not the sun."

ENTRY = LINE1 + "\n" + LINE2


def main():
    # Keep the sealed gate self-checking: 1-400 chars, exactly two lines,
    # one sentence each, no trailing newline.
    assert 1 <= len(ENTRY) <= 400, "entry outside 1-400 char gate"
    assert ENTRY.count("\n") == 1 and not ENTRY.endswith("\n")
    assert all(line.count(".") == 1 for line in ENTRY.split("\n"))
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
