# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    h = data[1:1 + n]
    print(max(h))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
