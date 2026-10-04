# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def color(a, b):
    if a == b == 0:
        return -1
    if a == 0:
        return 0
    if b == 0:
        return 1

    total = 0
    while a != b:
        high = a
        low = b
        if high < low:
            high, low = low, high

        q = high // low
        rem = high % low
        total += q

        if rem == 0:
            total -= 1
            break

        a = low
        b = rem

    return (total + 2) % 3


def solve_case(a, b):
    required = -1
    for x, y in zip(a, b):
        current = color(x, y)
        if current == -1:
            continue
        if required == -1:
            required = current
        if required != current:
            return "NO"
    return "YES"


def solve():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    index = 0
    cases = tokens[index]
    index += 1
    lines = []

    for _ in range(cases):
        n = tokens[index]
        index += 1
        left = tokens[index:index + n]
        index += n
        right = tokens[index:index + n]
        index += n
        lines.append(solve_case(left, right))

    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
solve()
