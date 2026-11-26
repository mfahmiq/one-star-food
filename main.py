"""One Star, Five Stars for the Food — make.fun entry.

Competition: u-po-pu-one-star-five-stars-for-the-food-f9166ee7 ($2).
Brief: one sentence, at most 200 characters — an alien tourist's
one-star review of Earth that still slips in a compliment about
the food.

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

This module writes ENTRY to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt) and self-verifies the result: UTF-8, 1-200 chars,
single line, no leading/trailing whitespace, and re-reads the written
file to confirm it is byte-identical. Exits non-zero on any failure.
"""

import os
import sys

# The entry text. Exactly one sentence, 135 characters, no trailing
# newline in the file — the written bytes are ENTRY encoded as UTF-8.
ENTRY = (
    "One star: Earth's gravity doubled my body weight the moment I "
    "landed, yet the dumplings were so good I nearly forgave the whole "
    "planet."
)

# Brief limits: one sentence, at most 200 characters.
MAX_CHARS = 200


def entry_text() -> str:
    """Return the champion entry text, unchanged from entry.txt."""
    return ENTRY


def validate_entry(text: str) -> str | None:
    """Check *text* against the brief; return an error string or None."""
    if not text or not text.strip():
        return "entry is empty or whitespace-only"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if not 1 <= len(text) <= MAX_CHARS:
        return f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        return f"entry is not UTF-8: {exc}"
    return None


def output_path() -> str:
    """Resolve the entry.txt path from MAKEFUN_OUTPUT_DIR (default /output)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def is_single_sentence(text: str) -> bool:
    """True when *text* reads as exactly one sentence.

    The brief asks for one sentence: a single terminal full stop,
    with no other sentence-ending punctuation inside.
    """
    body = text.rstrip(".")
    return text.endswith(".") and not any(ch in body for ch in ".!?")

def verify_output(path: str, expected: bytes) -> str | None:
    """Re-read *path* and check it against *expected*; error or None."""
    with open(path, "rb") as fh:
        written = fh.read()
    if written != expected:
        return "written file is not byte-identical to ENTRY"
    text = written.decode("utf-8")
    if text != expected.decode("utf-8"):
        return "re-read verification failed"
    if not 1 <= len(text) <= MAX_CHARS:
        return f"re-read entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    if not text.strip():
        return "re-read entry is whitespace-only"
    if not is_single_sentence(text):
        return "re-read entry is not a single sentence"
    return None


def main() -> int:
    text = entry_text()
    error = validate_entry(text)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1
    if not is_single_sentence(text):
        print("error: entry is not a single sentence", file=sys.stderr)
        return 1

    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)

    # Re-read and confirm byte-identical via the standalone verifier.
    error = verify_output(path, data)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(text)} chars")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
