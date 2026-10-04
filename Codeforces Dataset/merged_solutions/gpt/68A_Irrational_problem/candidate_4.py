# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    v = list(map(int, sys.stdin.read().split()))
    p = v[:4]
    a, b = v[4], v[5]

    m = min(p)
    r = min(b, m - 1)

    print(max(0, r - a + 1))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
