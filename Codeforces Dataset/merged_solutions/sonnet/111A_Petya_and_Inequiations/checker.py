"""111A accepts any n positive integers with sum <= y and sum of squares >= x.

Feasibility is decided by the extreme distribution: n-1 ones and a head of
y-(n-1), which maximises the sum of squares for a fixed total, so the answer is
-1 exactly when that distribution fails.
"""


def check_for(stdin, expected):
    n, x, y = (int(v) for v in stdin.split()[:3])
    head = y - (n - 1)
    feasible = head >= 1 and head * head + (n - 1) >= x

    def check(out):
        tokens = out.split()
        if not feasible:
            assert tokens == ["-1"], f"answer is -1, got {tokens[:5]}"
            return
        assert tokens != ["-1"], "printed -1 but a valid assignment exists"
        assert len(tokens) == n, f"expected {n} numbers, got {len(tokens)}"
        values = [int(v) for v in tokens]
        assert all(v >= 1 for v in values), "all numbers must be positive"
        assert sum(values) <= y, f"sum {sum(values)} exceeds y={y}"
        squares = sum(v * v for v in values)
        assert squares >= x, f"sum of squares {squares} is below x={x}"

    return check
