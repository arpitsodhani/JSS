import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: prime_counts :: (limit: int) -> list[int] ---
def prime_counts(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    stride = 2
    while stride * stride <= limit:
        if sieve[stride]:
            sieve[stride * stride::stride] = bytearray(len(sieve[stride * stride::stride]))
        stride += 1
    counts = [0] * (limit + 1)
    seen = 0
    for value in range(limit + 1):
        seen += sieve[value]
        counts[value] = seen
    return counts


# --- clause: lonely_count :: (n: int, counts: list[int]) -> int ---
def lonely_count(n, counts):
    root = int(n ** 0.5)
    while root * root > n:
        root -= 1
    while (root + 1) * (root + 1) <= n:
        root += 1
    return 1 + counts[n] - counts[root]


# --- clause: main :: () -> None ---
def main():
    queries = read_input()
    counts = prime_counts(max(queries) if queries else 1)
    out = []
    for n in queries:
        out.append(lonely_count(n, counts))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
