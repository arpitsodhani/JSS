# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    n = int(sys.stdin.readline())
    ans = 0

    while n > 1:
        ans += n
        p = 2
        while p * p <= n and n % p:
            p += 1
        if p * p > n:
            n = 1
        else:
            n //= p

    ans += 1
    print(ans)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
