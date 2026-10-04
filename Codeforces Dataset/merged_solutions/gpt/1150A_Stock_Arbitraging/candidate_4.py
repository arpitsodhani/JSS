# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mn = min(s)
    mx = max(b)

    if mx <= mn:
        print(r)
    else:
        shares = r // mn
        print((r % mn) + shares * mx)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
