# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from math import gcd

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    ans = []

    for k in data[1:1 + t]:
        ans.append(str(100 // gcd(k, 100)))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
