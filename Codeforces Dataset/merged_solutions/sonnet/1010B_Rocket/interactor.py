"""Judge side of 1010B, an interactive problem.

The rocket hides the distance x and the truth pattern p: the i-th question is
answered honestly when p[i mod n] is 1 and with the sign flipped otherwise. The
run has to end with the program receiving a 0, within 60 questions.
"""
import random


def tests():
    rng = random.Random(1010)
    cases = []
    for m, n in ((1, 1), (5, 2), (10, 3), (2, 30), (1000, 7), (10 ** 9, 30), (10 ** 9, 1)):
        for _ in range(3):
            x = rng.randint(1, m)
            pattern = [rng.randint(0, 1) for _ in range(n)]
            cases.append((m, n, x, pattern))
    # the corners: x at either end of the range, and a rocket that always lies
    cases.append((10 ** 9, 30, 1, [0] * 30))
    cases.append((10 ** 9, 30, 10 ** 9, [0] * 30))
    cases.append((10 ** 9, 30, 10 ** 9, [1] * 30))
    cases.append((1, 1, 1, [0]))
    return cases


def interact(case, send, readline):
    m, n, x, pattern = case
    send("%d %d" % (m, n))
    asked = 0
    while True:
        line = readline()
        assert line, f"m={m} n={n}: blank line from the program"
        y = int(line.split()[0])
        asked += 1
        assert asked <= 60, f"m={m} n={n}: asked {asked} questions, the budget is 60"
        assert 1 <= y <= m, f"question {y} outside 1..{m}"
        truth = 0 if y == x else (1 if x > y else -1)
        send(str(truth if pattern[(asked - 1) % n] else -truth))
        if truth == 0:
            break
