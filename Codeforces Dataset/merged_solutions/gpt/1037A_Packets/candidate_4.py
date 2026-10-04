# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    n = int(input())
    ans = 0
    v = 1
    while v <= n:
        v <<= 1
        ans += 1
    print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
