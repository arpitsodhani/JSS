# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    positions = []
    for index, amount in enumerate(values[1:n + 1]):
        if amount:
            positions.append(index)

    total = len(positions)
    if total == 1:
        return "-1"

    divisors = set()
    remaining = total
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            divisors.add(factor)
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        divisors.add(remaining)

    minimum = 10 ** 30
    for size in divisors:
        cost = 0
        for left in range(0, total, size):
            middle = left + size // 2
            base = positions[middle]
            segment = positions[left:left + size]
            cost += sum(abs(place - base) for place in segment)
        if cost < minimum:
            minimum = cost

    return str(minimum)

# CLAUSE: finish_program
sys.stdout.write(solve())
