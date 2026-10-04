"""Judge side of 1486C1, an interactive problem.

The jury hides a permutation; "? l r" is answered with the position of the
second largest element of that subsegment. The run must end with "! p" naming
the position of the maximum, inside the 40-query budget.
"""
import random


def tests():
    rng = random.Random(1486)
    cases = []
    for n in (2, 3, 5, 10, 64, 100, 1000, 100000):
        for _ in range(2):
            values = list(range(1, n + 1))
            rng.shuffle(values)
            cases.append(values)
    cases.append([1, 2])
    cases.append([2, 1])
    cases.append(list(range(1, 51)))
    cases.append(list(range(50, 0, -1)))
    return cases


def interact(case, send, readline):
    n = len(case)
    top = case.index(max(case)) + 1
    send(str(n))
    asked = 0
    while True:
        line = readline()
        assert line, f"n={n}: blank line from the program"
        parts = line.split()
        if parts[0] == "?":
            asked += 1
            assert asked <= 40, f"n={n}: asked {asked} queries, the budget is 40"
            l = int(parts[1])
            r = int(parts[2])
            assert 1 <= l < r <= n, f"n={n}: bad query {l} {r}"
            window = sorted(range(l - 1, r), key=lambda i: -case[i])
            send(str(window[1] + 1))
        elif parts[0] == "!":
            assert int(parts[1]) == top, f"n={n}: answered {parts[1]}, the maximum is at {top}"
            break
        else:
            raise AssertionError(f"unexpected line {line!r}")
