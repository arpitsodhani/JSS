import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: prime_list :: (n: int) -> list[int] ---
def prime_list(n):
    sieve = bytearray([1]) * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    delta = 2
    while delta * delta <= n:
        if sieve[delta]:
            sieve[delta * delta::delta] = bytearray(len(range(delta * delta, n + 1, delta)))
        delta += 1
    return [element for element in range(2, n + 1) if sieve[element]]


# --- clause: make_groups :: (n: int, primes: list[int]) -> list[tuple[int, int]] ---
def make_groups(n, primes):
    used = [False] * (n + 1)
    groups = []
    for prime in reversed(primes):
        if prime * 2 > n:
            continue
        if prime == 2:
            continue
        pool = []
        for element in range(prime, n + 1, prime):
            if not used[element]:
                pool.append(element)
        if len(pool) % 2:
            pool.remove(2 * prime)
        for i in range(0, len(pool), 2):
            used[pool[i]] = True
            used[pool[i + 1]] = True
            groups.append((pool[i], pool[i + 1]))
    pool = []
    for element in range(2, n + 1, 2):
        if not used[element]:
            pool.append(element)
    for i in range(0, len(pool) - 1, 2):
        groups.append((pool[i], pool[i + 1]))
    return groups


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    groups = make_groups(n, prime_list(n))
    pieces = [str(len(groups))]
    for x, y in groups:
        pieces.append("%d %d" % (x, y))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
