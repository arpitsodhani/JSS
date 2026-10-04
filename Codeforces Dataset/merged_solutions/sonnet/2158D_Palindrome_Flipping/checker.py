"""2158D accepts any operation sequence within the limit, so replay it.

Each printed operation must name a substring that is a palindrome at the moment
it is applied, the count must fit in [0, 2n], and the string must equal t at the
end. Brute force over every string of length 4..6 shows the whole space is one
connected component, so -1 is never a correct answer under the n>=4 constraint.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    pos = 1
    cases = []
    for _ in range(int(tokens[0])):
        n = int(tokens[pos])
        cases.append((n, tokens[pos + 1], tokens[pos + 2]))
        pos += 3

    def check(out):
        got = out.split()
        at = 0
        for case_no, (n, s, t) in enumerate(cases, start=1):
            assert at < len(got), f"case {case_no}: output ended early"
            k = int(got[at])
            at += 1
            assert k >= 0, f"case {case_no}: reported -1, but every n>=4 instance is solvable"
            assert k <= 2 * n, f"case {case_no}: {k} operations exceeds the limit of {2 * n}"
            cur = list(s)
            for step in range(k):
                assert at + 1 < len(got), f"case {case_no}: operation {step + 1} is truncated"
                l = int(got[at])
                r = int(got[at + 1])
                at += 2
                assert 1 <= l < r <= n, f"case {case_no} op {step + 1}: ({l}, {r}) out of range"
                piece = cur[l - 1:r]
                assert piece == piece[::-1], (
                    f"case {case_no} op {step + 1}: s[{l}..{r}] = {''.join(piece)} is not a palindrome")
                for x in range(l - 1, r):
                    cur[x] = "1" if cur[x] == "0" else "0"
            assert "".join(cur) == t, f"case {case_no}: ended at {''.join(cur)}, wanted {t}"
        assert at == len(got), f"{len(got) - at} unread tokens at the end of the output"

    return check
