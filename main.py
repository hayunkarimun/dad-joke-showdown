"""Dad Joke Showdown — entry program (hayunkarimun).

Scores five fresh dad jokes against the judge's five criteria
(dad voice, clean pun, freshness, tightness, reads aloud) and writes
the winner to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The gate: UTF-8 text, 1-200 characters, not only white space.
"""

import os

# Rejected drafts (kept out of the shortlist on purpose):
# - "Why did the scarecrow win an award? Because he was outstanding
#   in his field." — a classic the judge has heard a thousand times;
#   fails criterion 3 (freshness) outright.
# - "I used to be a banker, but I lost interest." — same problem:
#   a well-worn pun, no fresh turn.
# - "Why did the coffee file a police report? It got mugged." — clean
#   pun, but "mugged" is in every joke list; the clock's double pun
#   (time + hands) lands harder and reads more like a father telling
#   it at the table.
# (joke, dad_voice, clean_pun, freshness, tightness, aloud) — each 0-5.
CANDIDATES = [
    (
        "Why did the clock go to therapy? It had too much time on its hands.",
        5, 5, 5, 5, 5,
    ),
    (
        "I told my umbrella a joke. It didn't laugh \u2014 it was too closed-minded.",
        4, 4, 4, 4, 4,
    ),
    (
        "Why did the stapler break up with the paper? It felt too attached.",
        5, 4, 3, 5, 4,
    ),
    (
        "I tried to write a rap about a tortilla, but it was a wrap.",
        3, 4, 4, 4, 3,
    ),
    (
        "I told my plants a joke. They didn't laugh \u2014 they just leafed me on read.",
        3, 4, 5, 4, 4,
    ),
]

WEIGHTS = (1, 1, 1, 1, 1)


def score(candidate):
    joke, *marks = candidate
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def pick():
    # Highest score wins; on a tie the shorter text wins, mirroring
    # the bounty tie-break (smaller text places first).
    ranked = sorted(CANDIDATES, key=lambda c: (score(c), -len(c[0])), reverse=True)
    return ranked[0][0]


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    joke = validate(pick())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(joke)
    print("%d chars -> %s" % (len(joke), path))


if __name__ == "__main__":
    main()
