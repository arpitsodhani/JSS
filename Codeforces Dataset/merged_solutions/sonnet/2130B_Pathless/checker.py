"""2130B accepts any rearrangement Alice cannot use to reach the sum s.

Alice's walk visits every cell at least once, so the smallest reachable sum is
the array total; from there she can add any non-negative combination of the
adjacent-pair sums. The checker recomputes reachability with a small closure over
sums up to s.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        s = data[pos + 1]
        pos += 2
        cases.append((n, s, data[pos:pos + n]))
        pos += n

    def alice_can(order, s):
        total = sum(order)
        if s < total:
            return False
        need = s - total
        steps = {order[i] + order[i + 1] for i in range(len(order) - 1)}
        steps.discard(0)
        reach = [False] * (need + 1)
        reach[0] = True
        for value in range(need + 1):
            if not reach[value]:
                continue
            for step in steps:
                if value + step <= need:
                    reach[value + step] = True
        return reach[need]

    def check(out):
        tokens = out.split()
        at = 0
        for n, s, a in cases:
            if tokens[at] == "-1":
                at += 1
                # every arrangement must let Alice win
                from itertools import permutations
                shapes = set(permutations(a))
                for order in shapes:
                    assert alice_can(list(order), s), (
                        f"printed -1 but arrangement {order} blocks Alice")
                continue
            order = [int(v) for v in tokens[at:at + n]]
            at += n
            assert sorted(order) == sorted(a), "not a rearrangement"
            assert not alice_can(order, s), f"Alice can still reach {s} in {order}"
        assert at == len(tokens), "extra output"

    return check
