# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    n = int(input().strip())
    r = n % 10

    if r <= 5:
        print(n - r)
    else:
        print(n + (10 - r))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
