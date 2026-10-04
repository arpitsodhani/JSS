# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    n, k, t = map(int, sys.stdin.read().split())

    filled = n * k * t // 100
    ans = []

    for _ in range(n):
        x = min(k, filled)
        ans.append(str(x))
        filled -= x

    print(" ".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
