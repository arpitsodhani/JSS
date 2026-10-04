# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    a = list(map(int, sys.stdin.read().split()))
    n = a[0]
    h = a[1:]

    h[0] = 1
    h[-1] = 1

    for i in range(1, n):
        h[i] = min(h[i], h[i - 1] + 1)

    for i in range(n - 2, -1, -1):
        h[i] = min(h[i], h[i + 1] + 1)

    print(max(h))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
