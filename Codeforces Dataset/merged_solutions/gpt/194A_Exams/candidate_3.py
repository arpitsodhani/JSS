# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def solve():
        n, k = map(int, sys.stdin.buffer.read().split())
        for twos in range(n + 1):
            rest = n - twos
            rem = k - 2 * twos
            if 3 * rest <= rem <= 5 * rest:
                print(twos)
                return

    solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
