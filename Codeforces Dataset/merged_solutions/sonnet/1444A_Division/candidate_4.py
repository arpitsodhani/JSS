import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
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
        rest = p
        keep = 1
        while rest % prime == 0:
            rest //= prime
            keep *= prime
        value = rest
        for _ in range(power - 1):
            value *= prime
        if value > best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for p, q in read_input():
        out.append(biggest_divisor(p, q))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
