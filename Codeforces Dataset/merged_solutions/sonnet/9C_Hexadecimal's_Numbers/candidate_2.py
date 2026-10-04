# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    n = int(sys.stdin.readline())
    total = 0
    stack = [1]
    while stack:
        value = stack.pop()
        if value <= n:
            total += 1
            stack.append(value * 10)
            stack.append(value * 10 + 1)

# CLAUSE: finish_program
    print(total)

main()
