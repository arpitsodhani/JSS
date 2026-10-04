# CLAUSE: setup_environment
import sys

def first_prime_factor(n):
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n

def remove_factor(n, p):
    while n % p == 0:
        n //= p
    return n

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
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
