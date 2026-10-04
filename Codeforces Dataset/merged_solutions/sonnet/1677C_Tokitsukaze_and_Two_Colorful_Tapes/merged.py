import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        first = [int(token) for token in data[pos:pos + n]]
        pos += n
        second = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((n, first, second))
    return cases

# Clause best_beauty [Confidence: 1.00]
def best_beauty(n, first, second):
    nxt = [0] * (n + 1)
    for i in range(n):
        nxt[first[i]] = second[i]
    seen = [False] * (n + 1)
    pairs = 0
    for start in range(1, n + 1):
        if seen[start]:
            continue
        length = 0
        node = start
        while not seen[node]:
            seen[node] = True
            node = nxt[node]
            length += 1
        pairs += length // 2
    return 2 * pairs * (n - pairs)

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, first, second in read_input():
        out.append(str(best_beauty(n, first, second)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

