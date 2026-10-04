"""1255B accepts any cheapest set of chains, so the plan is validated directly.

A fridge stays private only when its chains lead to at least two different
neighbours; the printed cost has to match both the chains and the reference.
"""


def check_for(stdin, expected):
    data = stdin.split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        pos += 2
        cases.append((n, m, [int(v) for v in data[pos:pos + n]]))
        pos += n
    wanted = [line.strip() for line in expected.split("\n") if line.strip()]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        at = 0
        want_at = 0
        for n, m, weights in cases:
            head = rows[at]
            at += 1
            if wanted[want_at] == "-1":
                assert head == "-1", "printed a plan where none exists"
                want_at += 1
                continue
            assert head != "-1", "a plan exists but -1 was printed"
            cost = int(head)
            assert cost == int(wanted[want_at]), f"cost {cost}, cheapest is {wanted[want_at]}"
            neighbours = [set() for _ in range(n + 1)]
            spent = 0
            for _ in range(m):
                u, v = (int(x) for x in rows[at].split())
                at += 1
                assert u != v, "a chain must join two different fridges"
                spent += weights[u - 1] + weights[v - 1]
                neighbours[u].add(v)
                neighbours[v].add(u)
            assert spent == cost, f"chains cost {spent}, printed {cost}"
            for fridge in range(1, n + 1):
                assert len(neighbours[fridge]) >= 2, f"fridge {fridge} is not private"
            want_at += 1 + m

    return check
