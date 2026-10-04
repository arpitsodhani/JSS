import sys

LIMIT = 31624


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [(int(data[3 * i + 1]), int(data[3 * i + 2]), int(data[3 * i + 3]))
            for i in range(t)]


# --- clause: small_primes :: () -> list[int] ---
def small_primes():
    sieve = bytearray([1]) * LIMIT
    sieve[0] = 0
    sieve[1] = 0
    step = 2
    while step * step < LIMIT:
        if sieve[step]:
            sieve[step * step::step] = bytearray(len(range(step * step, LIMIT, step)))
        step += 1
    return [i for i in range(2, LIMIT) if sieve[i]]


# --- clause: factor_count :: (value: int, primes: list[int]) -> int ---
def factor_count(value, primes):
    total = 0
    for p in primes:
        if p * p > value:
            break
        while value % p == 0:
            value //= p
            total += 1
    if value > 1:
        total += 1
    return total


# --- clause: reachable :: (a: int, b: int, k: int, primes: list[int]) -> str ---
def reachable(a, b, k, primes):
    top = factor_count(a, primes)
    top += factor_count(b, primes)
    if top < k:
        return "NO"
    if k == 1:
        if a != b and (a % b == 0 or b % a == 0):
            return "YES"
        return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    primes = small_primes()
    out = []
    for case in read_input():
        out.append(reachable(case[0], case[1], case[2], primes))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
