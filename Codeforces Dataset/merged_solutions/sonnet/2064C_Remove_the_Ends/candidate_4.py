# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(a):
    suffix_neg = 0
    for value in a:
        if value < 0:
            suffix_neg -= value

    prefix_pos = 0
    answer = suffix_neg
    for value in a:
        if value > 0:
            prefix_pos += value
        else:
            suffix_neg += value
        candidate = prefix_pos + suffix_neg
        if candidate > answer:
            answer = candidate
    return answer

def solve():
    values = tuple(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    tests = values[pos]
    pos += 1
    lines = []
    while tests:
        tests -= 1
        n = values[pos]
        pos += 1
        lines.append(str(solve_case(values[pos:pos + n])))
        pos += n
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
solve()
