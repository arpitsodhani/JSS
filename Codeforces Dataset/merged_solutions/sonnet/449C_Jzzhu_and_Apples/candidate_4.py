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
    jump = 2
    while jump * jump <= n:
        if sieve[jump]:
            sieve[jump * jump::jump] = bytearray(len(range(jump * jump, n + 1, jump)))
        jump += 1
    return [entry for entry in range(2, n + 1) if sieve[entry]]


# --- clause: make_groups :: (n: int, primes: list[int]) -> list[tuple[int, int]] ---
def make_groups(n, primes):
    owner = [0] * (n + 1)
    for prime in primes:
        if prime == 2:
            continue
        for value in range(prime, n + 1, prime):
            if owner[value] == 0 and value % 2:
                owner[value] = prime
    buckets = {}
    for value in range(3, n + 1, 2):
        if owner[value] == 0:
            continue
        buckets.setdefault(owner[value], []).append(value)
    groups = []
    spare = []
    for prime in buckets:
        pool = buckets[prime]
        if 2 * prime <= n:
            pool.append(2 * prime)
        if len(pool) % 2:
            pool.pop()
        for i in range(0, len(pool), 2):
            groups.append((pool[i], pool[i + 1]))
    used = [False] * (n + 1)
    for x, y in groups:
        used[x] = True
        used[y] = True
    for value in range(2, n + 1, 2):
        if not used[value]:
            spare.append(value)
    for i in range(0, len(spare) - 1, 2):
        groups.append((spare[i], spare[i + 1]))
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
