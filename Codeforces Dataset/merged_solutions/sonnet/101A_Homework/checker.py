"""101A accepts any deletion of at most k characters leaving the fewest letters.

The printed string has to be a subsequence of the original with at least n - k
characters, and its alphabet size has to match the reference answer.
"""


def check_for(stdin, expected):
    lines = stdin.split("\n")
    word = lines[0].strip()
    k = int(lines[1])
    best = int(expected.split("\n")[0])

    def check(out):
        rows = out.split("\n")
        count = int(rows[0].strip())
        kept = rows[1].strip() if len(rows) > 1 else ""
        assert count == best, f"left {count} distinct letters, the fewest is {best}"
        assert len(kept) >= len(word) - k, f"deleted {len(word) - len(kept)} characters, the limit is {k}"
        assert len(set(kept)) == count, "the printed count does not match the string"
        at = 0
        for ch in kept:
            at = word.index(ch, at) + 1
        assert len(kept) <= len(word), "the string grew"

    return check
