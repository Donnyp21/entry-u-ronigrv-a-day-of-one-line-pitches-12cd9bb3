"""A Day of One-Line Pitches — entry for make.fun's
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes one sentence (at most 240 characters) to the harness output
directory as entry.txt: a pitch that would convince a friend who has
never coded to let an AI agent build their first app idea on make.fun.
The sentence is a fixed string: no randomness, no network, no time,
no input — two runs produce the same bytes.
"""

import os

# The pitch. Persuasion: a concrete reason to say yes now (a working
# first version today, on make.fun), low risk (try it tonight before
# spending anything), plain words, no jargon, no overpromising —
# it promises a first version to try, not a finished product.
LINE = "Tell me your app idea in plain words and I'll have an agent build you a working first version on make.fun today, so you can try it tonight before you spend a cent or write a line of code."

MAX_CHARS = 240


def output_dir() -> str:
    """Where the harness collects the entry: the env dir it names, else /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT")
        or "/output"
    )


def sentence_count(line: str) -> int:
    """Sentence-ending periods, not counting the dot inside 'make.fun'."""
    return line.count(".") - line.count("make.fun")


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} characters, over the {MAX_CHARS} cap"
    assert sentence_count(line) == 1 and line.endswith("."), "the line must be a single sentence"
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()
