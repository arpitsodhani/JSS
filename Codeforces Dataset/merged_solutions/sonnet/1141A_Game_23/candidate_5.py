# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    n, m = map(int, sys.stdin.buffer.readline().split())
    if n == m:
        print(0)
        return
    if m % n != 0:
        print(-1)
        return

    target = m // n
    steps = 0
    divisors = (6, 3, 2)

    for divisor in divisors:
        while target % divisor == 0:
            target //= divisor
            steps += 2 if divisor == 6 else 1

    print(steps if target == 1 else -1)

# CLAUSE: finish_program
main()
