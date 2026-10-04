"""2003C accepts any reordering maximising the good pairs, so score the answer.

Spreading equal letters as far apart as possible - one of each distinct letter
per round - is optimal, so compare the good-pair count against that arrangement.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    cases = []
    pos = 1
    for _ in range(int(tokens[0])):
        n = int(tokens[pos])
        cases.append((n, tokens[pos + 1]))
        pos += 2

    def good_pairs(text):
        n = len(text)
        total = 0
        for i in range(n):
            for j in range(i + 1, n):
                if text[i] == text[j]:
                    total += 1
                    continue
                for k in range(i, j):
                    if text[k] != text[k + 1] and (text[k] != text[i] or text[k + 1] != text[j]):
                        total += 1
                        break
        return total

    def reference(s):
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        out = []
        while len(out) < len(s):
            for ch in sorted(counts):
                if counts[ch]:
                    out.append(ch)
                    counts[ch] -= 1
        return "".join(out)

    def check(out):
        got = out.split()
        assert len(got) == len(cases), f"expected {len(cases)} lines"
        for (n, s), answer in zip(cases, got):
            assert sorted(answer) == sorted(s), f"{answer} is not a reordering of {s}"
            best = good_pairs(reference(s))
            assert good_pairs(answer) == best, (
                f"{answer} has {good_pairs(answer)} good pairs, the best is {best}")

    return check
