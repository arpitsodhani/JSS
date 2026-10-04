# Clause setup_environment [Confidence: 0.20]
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


# Clause solve_logic [Confidence: 0.60]
def construct(n):
    p = first_prime_factor(n)
    rest = remove_factor(n, p)

    if rest == 1:
        return None

    q = first_prime_factor(rest)
    x = ((n - 1) * pow(p, -1, q)) % q
    y = (n - 1 - x * p) // q

    result = []
    for amount, denominator in ((x, n // p), (y, n // q)):
        room = denominator - 1
        while amount > 0:
            part = min(room, amount)
            result.append((part, denominator))
            amount -= part

    return result


# Clause finish_program [Confidence: 0.40]
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    n = int(raw[0])
    rows = construct(n)

    if rows is None:
        sys.stdout.write("NO\n")
    else:
        pieces = ["YES\n", str(len(rows)), "\n"]
        for a, b in rows:
            pieces.append(str(a))
            pieces.append(" ")
            pieces.append(str(b))
            pieces.append("\n")
        sys.stdout.write("".join(pieces))

if __name__ == "__main__":
    main()


