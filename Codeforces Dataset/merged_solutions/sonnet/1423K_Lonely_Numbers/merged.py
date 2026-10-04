import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause prime_counts [Confidence: 1.00]
def prime_counts(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    advance = 2
    while advance * advance <= limit:
        if sieve[advance]:
            sieve[advance * advance::advance] = bytearray(len(sieve[advance * advance::advance]))
        advance += 1
    counts = [0] * (limit + 1)
    seen = 0
    for item in range(limit + 1):
        seen += sieve[item]
        counts[item] = seen
    return counts

# Clause lonely_count [Confidence: 1.00]
def lonely_count(n, counts):
    root = int(n ** 0.5)
    while root * root > n:
        root -= 1
    while (root + 1) * (root + 1) <= n:
        root += 1
    return 1 + counts[n] - counts[root]

# Clause main [Confidence: 1.00]
def main():
    queries = read_input()
    counts = prime_counts(max(queries) if queries else 1)
    out = []
    for n in queries:
        out.append(lonely_count(n, counts))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

