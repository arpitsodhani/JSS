# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def best_frequency(values):
    seen = defaultdict(int)
    maximum = 0
    for item in values:
        seen[item] += 1
        maximum = max(maximum, seen[item])
    return maximum

def clone_cost(size, amount):
    swaps = 0
    current = amount
    while current != size:
        grow = min(current, size - current)
        swaps += 1
        swaps += grow
        current += grow
    return swaps

def main():
    items = sys.stdin.buffer.read().split()
    case_count = int(items[0])
    cursor = 1
    lines = []
    for _ in range(case_count):
        n = int(items[cursor])
        cursor += 1
        segment = items[cursor:cursor + n]
        cursor += n
        lines.append(str(clone_cost(n, best_frequency(segment))))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
main()
