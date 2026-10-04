# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    n = int(input())
    print((3 * n * n - n) // 2)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
