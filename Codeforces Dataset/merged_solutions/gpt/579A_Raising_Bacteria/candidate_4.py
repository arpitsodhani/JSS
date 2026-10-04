# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    x = int(input())
    print(x.bit_count())

# CLAUSE: finish_program
def main():
    _inner_main()

main()
