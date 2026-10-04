# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    n = int(input())
    if n == 1:
        print(1)
    else:
        ans = 3 * n * n - n - 1
        if n >= 3:
            ans = max(ans, 5 * (n * n - n - 1))
            ans = max(ans, 4 * n * n - n - 4)
        print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
