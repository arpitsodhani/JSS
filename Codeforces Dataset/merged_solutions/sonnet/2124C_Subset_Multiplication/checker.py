"""2124C accepts any x that some beautiful a and subset S could have produced.

Whether an x works is decided by a two-state scan over b: each index is either
scaled by x or not, index i may be scaled only when x divides b_i, and adjacent
choices must keep a_i dividing a_{i+1}.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    t = int(tokens[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(tokens[pos])
        pos += 1
        cases.append([int(v) for v in tokens[pos:pos + n]])
        pos += n

    def feasible(b, x):
        reach = [True, b[0] % x == 0]
        for i in range(len(b) - 1):
            nxt = [False, False]
            for scaled_here in (0, 1):
                if not reach[scaled_here]:
                    continue
                left = b[i] // x if scaled_here else b[i]
                for scaled_next in (0, 1):
                    if scaled_next and b[i + 1] % x:
                        continue
                    right = b[i + 1] // x if scaled_next else b[i + 1]
                    if right % left == 0:
                        nxt[scaled_next] = True
            reach = nxt
        return reach[0] or reach[1]

    def check(out):
        got = out.split()
        assert len(got) == len(cases), f"expected {len(cases)} numbers, got {len(got)}"
        for idx, (b, raw) in enumerate(zip(cases, got), start=1):
            x = int(raw)
            assert 1 <= x <= 10 ** 9, f"case {idx}: x={x} is out of range"
            assert feasible(b, x), f"case {idx}: x={x} admits no beautiful array"

    return check
