# CLAUSE: setup_environment
import sys

def two_distinct_primes(n):
    first = 0
    x = n

    if x % 2 == 0:
        first = 2
        while x % 2 == 0:
            x //= 2

    d = 3
    while d * d <= x:
        if x % d == 0:
            if first:
                return first, d
            first = d
            while x % d == 0:
                x //= d
        d += 2

    if x > 1 and first:
        return first, x

    return None

def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    while r:
        t = old_r // r
        old_r, r = r, old_r - t * r
        old_s, s = s, old_s - t * s
    return old_s

# CLAUSE: solve_logic
def solve(n):
    pair = two_distinct_primes(n)
    if pair is None:
        return ["NO"]

    p, q = pair
    inv = extended_gcd(p, q) % q
    x = ((n - 1) * inv) % q
    y = (n - 1 - p * x) // q

    lines = []
    stack = [(x, n // p), (y, n // q)]

    for count, den in stack:
        limit = den - 1
        while count > 0:
            take = limit if count > limit else count
            lines.append((take, den))
            count -= take

    out = ["YES", str(len(lines))]
    for a, b in lines:
        out.append(str(a) + " " + str(b))
    return out

# CLAUSE: finish_program
def main():
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return
    result = solve(int(tokens[0]))
    print("\n".join(result))

if __name__ == "__main__":
    main()
