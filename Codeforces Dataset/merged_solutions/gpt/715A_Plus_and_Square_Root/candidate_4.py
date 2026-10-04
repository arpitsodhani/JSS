# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    n = int(input())
    for i in range(1, n + 1):
        if i == 1:
            print(2)
        else:
            print(i * (i + 1) * (i + 1) - i + 1)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
