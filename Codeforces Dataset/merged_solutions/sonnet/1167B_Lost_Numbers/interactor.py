"""Judge side of 1167B, an interactive problem.

The jury hides a permutation of 4, 8, 15, 16, 23 and 42; "? i j" is answered
with a_i * a_j, at most four times, and the run ends with "! ..." naming the
whole array.
"""
import itertools
import random


def tests():
    values = [4, 8, 15, 16, 23, 42]
    cases = [list(p) for p in itertools.permutations(values)]
    rng = random.Random(1167)
    rng.shuffle(cases)
    return cases[:40] + [values, values[::-1]]


def interact(case, send, readline):
    asked = 0
    while True:
        line = readline()
        assert line, "blank line from the program"
        parts = line.split()
        if parts[0] == "?":
            asked += 1
            assert asked <= 4, f"asked {asked} queries, the budget is 4"
            i = int(parts[1])
            j = int(parts[2])
            assert 1 <= i <= 6 and 1 <= j <= 6, f"bad query {line!r}"
            send(str(case[i - 1] * case[j - 1]))
        elif parts[0] == "!":
            got = [int(v) for v in parts[1:]]
            assert got == case, f"answered {got}, the array is {case}"
            break
        else:
            raise AssertionError(f"unexpected line {line!r}")
