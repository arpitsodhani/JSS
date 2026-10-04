# CLAUSE: setup_environment
import sys
from math import gcd

def distinct_prime_factors(value):
    found = []
    d = 2
    while d * d <= value:
        if value % d == 0:
            found.append(d)
            while value % d == 0:
                value //= d
        if d == 2:
            d = 3
        else:
            d += 2
    if value > 1:
        found.append(value)
    return found

# CLAUSE: solve_logic
def build_answer(n):
    primes = distinct_prime_factors(n)
    if len(primes) < 2:
        return None

    p, q = primes[0], primes[1]
    g = gcd(p, q)
    pp = p // g
    qq = q // g
    need = (n - 1) // g

    x = (need * pow(pp, -1, qq)) % qq
    y = (n - 1 - x * p) // q

    while y < 0:
        x += qq
        y = (n - 1 - x * p) // q

    ans = []
    b1 = n // p
    b2 = n // q

    while x:
        cur = min(x, b1 - 1)
        ans.append((cur, b1))
        x -= cur

    while y:
        cur = min(y, b2 - 1)
        ans.append((cur, b2))
        y -= cur

    return ans

# CLAUSE: finish_program
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    ans = build_answer(n)

    if ans is None:
        sys.stdout.write("NO\n")
        return

    out = ["YES", str(len(ans))]
    out.extend(f"{a} {b}" for a, b in ans)
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
