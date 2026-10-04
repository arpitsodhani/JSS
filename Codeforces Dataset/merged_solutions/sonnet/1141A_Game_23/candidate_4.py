# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
n = int(data[0])
m = int(data[1])
result = -1

if m % n == 0:
    value = m // n
    counts = []
    for factor in [3, 2]:
        current = 0
        while value % factor == 0:
            value //= factor
            current += 1
        counts.append(current)
    if value == 1:
        result = sum(counts)

# CLAUSE: finish_program
sys.stdout.write(str(result))
