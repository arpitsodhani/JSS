import sys

LIMIT = 31624


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    numbers = list(map(int, data[1:1 + 3 * t]))
    return list(zip(numbers[0::3], numbers[1::3], numbers[2::3]))


# --- clause: small_primes :: () -> list[int] ---
def small_primes():
    sieve = bytearray([1]) * LIMIT
    sieve[0:2] = b"\x00\x00"
    step = 2
    while step * step < LIMIT:
        if sieve[step]:
            sieve[step * step::step] = bytearray(len(range(step * step, LIMIT, step)))
        step += 1
    return [i for i in range(2, LIMIT) if sieve[i]]


# --- clause: factor_count :: (value: int, primes: list[int]) -> int ---
def factor_count(value, primes):
    total = 0
    rest = value
    for p in primes:
        if p * p > rest:
            break
        while rest % p == 0:
            rest = rest // p
            total = total + 1
    if rest > 1:
        total = total + 1
    return total


# --- clause: reachable :: (a: int, b: int, k: int, primes: list[int]) -> str ---
def reachable(a, b, k, primes):
    top = factor_count(a, primes) + factor_count(b, primes)
    if k > top:
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
    for a, b, k in read_input():
        out.append(reachable(a, b, k, primes))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
