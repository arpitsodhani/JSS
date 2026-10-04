"""2233C accepts any removal mask reaching the smallest possible cost.

The cost is twice the number of matched brackets left, so the printed mask is
scored that way and compared with the reference mask.
"""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        n = int(data[pos])
        k = int(data[pos + 1])
        s = data[pos + 2]
        pos += 3
        cases.append((n, k, s))
    reference = [line.strip() for line in expected.split("\n") if line.strip()]

    def cost(s, mask):
        depth = 0
        pairs = 0
        for ch, flag in zip(s, mask):
            if flag == "1":
                continue
            if ch == "(":
                depth += 1
            elif depth:
                depth -= 1
                pairs += 1
        return 2 * pairs

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        assert len(rows) == t, f"expected {t} lines, got {len(rows)}"
        for case in range(t):
            n, k, s = cases[case]
            mask = rows[case]
            assert len(mask) == n, f"case {case + 1}: mask has {len(mask)} characters, expected {n}"
            assert set(mask) <= set("01"), f"case {case + 1}: mask must be binary"
            assert mask.count("1") <= k, f"case {case + 1}: removed {mask.count('1')} characters, budget {k}"
            best = cost(s, reference[case])
            here = cost(s, mask)
            assert here <= best, f"case {case + 1}: cost {here}, best is {best}"

    return check
