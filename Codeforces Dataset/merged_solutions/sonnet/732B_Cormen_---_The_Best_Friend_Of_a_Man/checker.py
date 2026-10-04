"""732B accepts any optimal schedule, so check the rules and the total.

b must dominate a, every consecutive pair must reach k, and the printed count
must be both the number of walks actually added and the true minimum. The
minimum is recomputed here by the same left-to-right argument the problem forces:
day i can only be repaired by raising b[i], since b[i-1] is already fixed by the
time the pair (i-1, i) is considered.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    n = int(tokens[0])
    k = int(tokens[1])
    a = [int(x) for x in tokens[2:2 + n]]
    best = list(a)
    optimum = 0
    for i in range(1, n):
        short = k - (best[i - 1] + best[i])
        if short > 0:
            best[i] += short
            optimum += short

    def check(out):
        got = out.split()
        assert len(got) == 1 + n, f"expected 1 + {n} numbers, got {len(got)}"
        total = int(got[0])
        b = [int(x) for x in got[1:]]
        assert total == optimum, f"reported {total} extra walks, the minimum is {optimum}"
        assert sum(b) - sum(a) == total, "the schedule does not add up to the reported total"
        for i in range(n):
            assert b[i] >= a[i], f"day {i + 1}: {b[i]} < already planned {a[i]}"
        for i in range(1, n):
            assert b[i - 1] + b[i] >= k, f"days {i} and {i + 1} total {b[i - 1] + b[i]} < {k}"

    return check
