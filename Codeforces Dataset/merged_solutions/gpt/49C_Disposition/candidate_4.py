# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    n = int(sys.stdin.readline())
    ans = list(range(2, n + 1)) + [1]
    print(*ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
