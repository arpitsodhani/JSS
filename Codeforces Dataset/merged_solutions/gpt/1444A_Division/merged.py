# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def solve():
    input = sys.stdin.readline
    t = int(input())
    ans = []

    for _ in range(t):
        p, q = map(int, input().split())

        if p % q != 0:
            ans.append(str(p))
            continue

        n = q
        factors = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                factors.append(d)
                while n % d == 0:
                    n //= d
            d += 1 if d == 2 else 2
        if n > 1:
            factors.append(n)

        best = 1
        for f in factors:
            x = p
            while x % q == 0:
                x //= f
            if x > best:
                best = x

        ans.append(str(best))

    print("\n".join(ans))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
