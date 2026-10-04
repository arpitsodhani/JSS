# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    if data:
        n = data[0]
        arr = data[1:1 + n]
        arr.sort()
        print(*arr)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
