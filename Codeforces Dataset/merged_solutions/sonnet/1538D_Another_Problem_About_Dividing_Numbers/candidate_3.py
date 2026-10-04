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
    sieve[0:2] = b"\x00\x00"
    for step in range(2, int(LIMIT ** 0.5) + 1):
        if sieve[step]:
            for multiple in range(step * step, LIMIT, step):
                sieve[multiple] = 0
    primes = []
    for i in range(2, LIMIT):
        if sieve[i]:
            primes.append(i)
    return primes


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
    top = factor_count(a, primes) + factor_count(b, primes)
    if k > top:
        return "NO"
    if k == 1:
        if a == b:
            return "NO"
        if a % b and b % a:
            return "NO"
        return "YES"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    primes = small_primes()
    out = []
    for a, b, k in read_input():
        out.append(reachable(a, b, k, primes))
    print("\n".join(out))


if __name__ == "__main__":
    main()
