# CLAUSE: setup_environment
import sys

input_stream = sys.stdin

def query_interval(bounds):
    left, right = bounds
    print("?", left, right)
    sys.stdout.flush()
    return int(input_stream.readline())

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
print("!", best)
sys.stdout.flush()
