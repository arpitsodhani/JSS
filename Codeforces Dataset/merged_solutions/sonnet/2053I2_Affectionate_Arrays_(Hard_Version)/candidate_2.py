# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    tokens = sys.stdin.buffer.read().split()
    pos = 0
    t = int(tokens[pos])
    pos += 1
    answers = []
    for _ in range(t):
        n = int(tokens[pos])
        pos += 1
        best = -10**30
        current = -10**30
        for _ in range(n):
            value = int(tokens[pos])
            pos += 1
            if current < 0:
                current = value
            else:
                current += value
            if current > best:
                best = current
        answers.append(str(best))
    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
solve()
