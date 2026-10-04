# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    a = data[2:]

    print(2, a[0], a[1])

# CLAUSE: finish_program
def main():
    _inner_main()

main()
