"""One Star, Five Stars for the Food — make.fun entry.

Entry (135 chars):
    One star: Earth's gravity doubled my body weight the moment I
    landed, yet the dumplings were so good I nearly forgave the whole
    planet.

Why it won the internal tournament (16 candidates, pairwise, judged
against the published brief in weight order):
  1. On subject: a one-star review of Earth from an alien tourist that
     still slips in a real compliment about the food.
  2. Sounds like a real alien visitor: gravity doubling an alien's body
     weight on landing is a bodily, outsider grievance worth one star —
     no human tourist complains about that.
  3. Lands the joke: the complaint and the compliment both hit, and the
     turn — "nearly forgave the whole planet" — ties the food back to
     the review itself, the biggest turn in the field.
  4. Tight: 135 characters, one sentence, every word earning its place.
  5. Fresh: a gravity grievance, not the generic rain/traffic/weather
     complaints other candidates carried.
It beat the runner-up ("One star: the oceans are just salt water
pretending to be a beach, but the street skewers were so good I forgot
I was still wet.") in the final on criteria 2 and 3: a grievance worth
one star, and a turn that lands harder.

Writes ENTRY to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
then self-verifies: UTF-8, 1-200 chars, single line, not whitespace-only,
no leading/trailing whitespace, and re-reads the written file to confirm
it is byte-identical. Exits non-zero on any failure.
"""

import os
import sys

ENTRY = (
    "One star: Earth's gravity doubled my body weight the moment I "
    "landed, yet the dumplings were so good I nearly forgave the whole "
    "planet."
)


def main() -> int:
    # MAKEFUN_OUTPUT_DIR is a directory; default /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")

    # Validate before writing.
    if not ENTRY or not ENTRY.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(f"error: entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry is not UTF-8: {exc}", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Re-read and confirm byte-identical.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: written file is not byte-identical to ENTRY", file=sys.stderr)
        return 1
    text = written.decode("utf-8")
    if text != ENTRY or not 1 <= len(text) <= 200 or not text.strip():
        print("error: re-read verification failed", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(ENTRY)} chars")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
