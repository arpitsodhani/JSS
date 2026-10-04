"""1554D accepts any string of length n in which every substring that occurs,
occurs an odd number of times.

The samples are short, so the checker simply counts every substring.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    sizes = data[1:1 + data[0]]

    def check(out):
        lines = out.split()
        assert len(lines) == len(sizes), f"expected {len(sizes)} strings, got {len(lines)}"
        for n, s in zip(sizes, lines):
            assert len(s) == n, f"expected length {n}, got {len(s)}"
            assert all("a" <= ch <= "z" for ch in s), f"{s!r} is not lowercase latin"
            counts = {}
            for i in range(n):
                for j in range(i + 1, n + 1):
                    piece = s[i:j]
                    counts[piece] = counts.get(piece, 0) + 1
            for piece, times in counts.items():
                assert times % 2 == 1, f"{s!r}: {piece!r} occurs {times} times"

    return check
