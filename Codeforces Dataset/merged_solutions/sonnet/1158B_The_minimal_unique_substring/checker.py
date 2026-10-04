"""1158B accepts any binary string of length n whose shortest unique substring is k.

The samples are short, so the checker just counts every substring occurrence and
reports the first length at which some substring occurs exactly once.
"""


def check_for(stdin, expected):
    n, k = (int(v) for v in stdin.split()[:2])

    def minimal_unique(s):
        for length in range(1, len(s) + 1):
            seen = {}
            for i in range(len(s) - length + 1):
                piece = s[i:i + length]
                seen[piece] = seen.get(piece, 0) + 1
            if any(count == 1 for count in seen.values()):
                return length
        return -1

    def check(out):
        s = out.strip()
        assert len(s) == n, f"expected a string of length {n}, got {len(s)}"
        assert set(s) <= {"0", "1"}, f"string has symbols other than 0/1: {s!r}"
        got = minimal_unique(s)
        assert got == k, f"minimal unique substring of {s!r} is {got}, expected {k}"

    return check
