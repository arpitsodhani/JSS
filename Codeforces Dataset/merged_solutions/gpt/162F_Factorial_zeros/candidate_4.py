# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    s = sys.stdin.read().strip()
    if s:
        n = int(s)
        ans = 0
        while n:
            n //= 5
            ans += n
        print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
