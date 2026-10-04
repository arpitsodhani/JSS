# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def is_prime(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    primes = []
    p = 2
    while len(primes) < 55:
        if is_prime(p):
            primes.append(p)
        p += 1

    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        g = 0
        for v in a:
            g = math.gcd(g, v)

        res = -1
        for p in primes:
            if g % p != 0:
                res = p
                break
        ans.append(str(res))

    print("\n".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
