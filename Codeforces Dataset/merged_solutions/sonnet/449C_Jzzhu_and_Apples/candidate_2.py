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
    stride = 2
    while stride * stride <= n:
        if sieve[stride]:
            sieve[stride * stride::stride] = bytearray(len(range(stride * stride, n + 1, stride)))
        stride += 1
    return [item for item in range(2, n + 1) if sieve[item]]


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
        for item in range(prime, n + 1, prime):
            if not used[item]:
                pool.append(item)
        if len(pool) % 2:
            pool.remove(2 * prime)
        for i in range(0, len(pool), 2):
            used[pool[i]] = True
            used[pool[i + 1]] = True
            groups.append((pool[i], pool[i + 1]))
    pool = []
    for item in range(2, n + 1, 2):
        if not used[item]:
            pool.append(item)
    for i in range(0, len(pool) - 1, 2):
        groups.append((pool[i], pool[i + 1]))
    return groups


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    groups = make_groups(n, prime_list(n))
    out = [str(len(groups))]
    for x, y in groups:
        out.append("%d %d" % (x, y))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
