import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 2 * i], data[2 + 2 * i]))
    return cases

# Clause prime_powers [Confidence: 1.00]
def prime_powers(q):
    rows = []
    d = 2
    while d * d <= q:
        if q % d == 0:
            power = 0
            while q % d == 0:
                q //= d
                power += 1
            rows.append((d, power))
        d += 1
    if q > 1:
        rows.append((q, 1))
    return rows

# Clause biggest_divisor [Confidence: 1.00]
def biggest_divisor(p, q):
    if p % q:
        return p
    best = 1
    for prime, power in prime_powers(q):
        here = p
        inside = 0
        while here % prime == 0:
            here //= prime
            inside += 1
        item = p
        for _ in range(inside - power + 1):
            item //= prime
        if item > best:
            best = item
    return best

# Clause main [Confidence: 1.00]
def main():
    out = []
    for p, q in read_input():
        out.append(biggest_divisor(p, q))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

