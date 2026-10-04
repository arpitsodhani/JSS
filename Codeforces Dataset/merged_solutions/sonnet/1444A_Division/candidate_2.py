import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 2 * i], tokens[2 + 2 * i]))
    return cases


# --- clause: prime_powers :: (q: int) -> list[tuple[int, int]] ---
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


# --- clause: biggest_divisor :: (p: int, q: int) -> int ---
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


# --- clause: main :: () -> None ---
def main():
    out = []
    for p, q in read_input():
        out.append(biggest_divisor(p, q))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
