"""Judge side of 1698D, an interactive problem.

The statement's sample is a transcript, so it cannot be fed as stdin. This plays
the jury: it hides an array built from disjoint swaps (leaving exactly one fixed
point), answers "? l r" with the sorted subarray, enforces the 15-query budget
and checks the reported position.
"""
import random


def tests():
    rng = random.Random(23)
    batch = []
    for n in (3, 3, 5, 7, 9, 15, 33, 101, 999, 4999, 9999):
        values = list(range(1, n + 1))
        order = list(range(n))
        rng.shuffle(order)
        order.pop()
        for i in range(0, len(order), 2):
            a = order[i]
            b = order[i + 1]
            values[a], values[b] = values[b], values[a]
        batch.append((n, values))
    # a couple of hand-made shapes as well
    batch.append((3, [1, 3, 2]))
    batch.append((5, [4, 2, 5, 1, 3]))
    return [batch]


def interact(case, send, readline):
    send(str(len(case)))
    for n, values in case:
        fixed = 0
        for i in range(n):
            if values[i] == i + 1:
                fixed = i + 1
        send(str(n))
        used = 0
        while True:
            line = readline()
            assert line, "blank line from the program"
            parts = line.split()
            if parts[0] == "?":
                used += 1
                assert used <= 15, f"n={n}: used {used} queries, the budget is 15"
                assert len(parts) == 3, f"malformed query {line!r}"
                l = int(parts[1])
                r = int(parts[2])
                assert 1 <= l <= r <= n, f"query [{l}, {r}] outside 1..{n}"
                send(" ".join(map(str, sorted(values[l - 1:r]))))
            elif parts[0] == "!":
                assert len(parts) == 2, f"malformed answer {line!r}"
                got = int(parts[1])
                assert got == fixed, f"n={n}: answered {got}, the fixed point is {fixed}"
                break
            else:
                raise AssertionError(f"unexpected line {line!r}")
