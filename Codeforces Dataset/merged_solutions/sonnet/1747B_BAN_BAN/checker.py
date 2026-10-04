"""1747B accepts any shortest sequence of swaps that kills every BAN subsequence.

ceil(n/2) swaps are necessary and sufficient, so check the count and replay.
"""


def check_for(stdin, expected):
    sizes = [int(v) for v in stdin.split()[1:]]

    def check(out):
        got = [int(v) for v in out.split()]
        at = 0
        for n in sizes:
            m = got[at]
            at += 1
            assert m == (n + 1) // 2, f"n={n}: used {m} swaps, the minimum is {(n + 1) // 2}"
            text = list("BAN" * n)
            for _ in range(m):
                i, j = got[at], got[at + 1]
                at += 2
                assert 1 <= i <= 3 * n and 1 <= j <= 3 * n and i != j, f"bad swap ({i}, {j})"
                text[i - 1], text[j - 1] = text[j - 1], text[i - 1]
            need = "BAN"
            k = 0
            for ch in text:
                if ch == need[k]:
                    k += 1
                    if k == 3:
                        break
            assert k < 3, f"n={n}: BAN is still a subsequence of {''.join(text)}"
        assert at == len(got), "trailing output"

    return check
