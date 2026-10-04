# Clause setup_environment [Confidence: 0.60]
import sys

read_line = sys.stdin.readline

def ask(left, right):
    print(f"? {left} {right}")
    sys.stdout.flush()
    return int(read_line())


# Clause solve_logic [Confidence: 0.60]
n = int(input_stream.readline())
best = 0
pending = [(1, n)]

while pending:
    left, right = pending.pop()
    if left == right:
        value = query_interval((left, right))
        if value > best:
            best = value
    else:
        middle = (left + right) // 2
        pending.append((middle + 1, right))
        pending.append((left, middle))


# Clause finish_program [Confidence: 0.60]
print(f"! {answer}")
sys.stdout.flush()


