# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(items, start):
    count = int(items[start])
    start += 1
    first = int(items[start])
    start += 1
    best_here = first
    best_total = first
    for end in range(start, start + count - 1):
        number = int(items[end])
        combined = best_here + number
        best_here = number if number > combined else combined
        if best_here > best_total:
            best_total = best_here
    return best_total, start + count - 1

def solve():
    parts = sys.stdin.buffer.read().split()
    cases = int(parts[0])
    pointer = 1
    lines = []
    for _ in range(cases):
        answer, pointer = solve_case(parts, pointer)
        lines.append(str(answer))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
solve()
