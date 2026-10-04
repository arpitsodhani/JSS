# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
def main():
    n = int(sys.stdin.readline())
    total = 0
    queue = deque([1])
    while queue:
        value = queue.popleft()
        if value > n:
            continue
        total += 1
        queue.append(value * 10)
        queue.append(value * 10 + 1)

# CLAUSE: finish_program
    sys.stdout.write(str(total))

main()
