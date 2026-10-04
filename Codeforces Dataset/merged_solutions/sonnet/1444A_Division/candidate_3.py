import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
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
    finest = 1
    for prime, power in prime_powers(q):
        here = p
        inside = 0
        while here % prime == 0:
            here //= prime
            inside += 1
        element = p
        for _ in range(inside - power + 1):
            element //= prime
        if element > finest:
            finest = element
    return finest


# --- clause: main :: () -> None ---
def main():
    out = []
    for p, q in read_input():
        out.append(biggest_divisor(p, q))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
