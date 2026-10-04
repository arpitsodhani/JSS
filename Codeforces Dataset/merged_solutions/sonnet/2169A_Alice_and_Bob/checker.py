"""2169A accepts any b maximising Bob's points, so score the answer.

Bob wins a marble when his number is strictly closer, so with b above a he takes
the marbles above the midpoint and with b below a the ones below it. The best he
can do is therefore max(#{v > a}, #{v < a}), reached at b = a+1 or b = a-1.
"""


def check_for(stdin, expected):
    tokens = stdin.split()
    cases = []
    pos = 1
    for _ in range(int(tokens[0])):
        n, a = int(tokens[pos]), int(tokens[pos + 1])
        pos += 2
        cases.append((a, [int(v) for v in tokens[pos:pos + n]]))
        pos += n

    def score(a, marbles, b):
        return sum(1 for v in marbles if abs(v - b) < abs(v - a))

    def check(out):
        got = [int(v) for v in out.split()]
        assert len(got) == len(cases), f"expected {len(cases)} answers, got {len(got)}"
        for (a, marbles), b in zip(cases, got):
            assert 0 <= b <= 2 * 10 ** 9, f"b={b} outside [0, 2e9]"
            best = max(score(a, marbles, a + 1), score(a, marbles, a - 1) if a >= 1 else 0)
            assert score(a, marbles, b) == best, (
                f"a={a}: b={b} scores {score(a, marbles, b)}, the best is {best}")

    return check
