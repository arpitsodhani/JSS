# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
n = int(sys.stdin.buffer.readline())
numbers = [1]
first = 3
numbers.append(first)
current = first
for _ in range(1, 10):
    current = (current - 1) ** 2 + 1
    extra = [value * current for value in numbers[1:]]
    numbers.extend(extra)
numbers.sort()

# CLAUSE: finish_program
sys.stdout.write(f"{numbers[n - 1]}\n")
