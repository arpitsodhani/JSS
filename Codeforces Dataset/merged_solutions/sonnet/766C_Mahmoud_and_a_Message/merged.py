import sys
MOD = 10 ** 9 + 7

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1].decode()
    limits = list(map(int, data[2:28]))
    return n, s, limits

# Clause reach [Confidence: 1.00]
def reach(n, s, limits):
    span = [0] * (n + 1)
    for end in range(1, n + 1):
        allowed = n
        best = 0
        for start in range(end, 0, -1):
            cap = limits[ord(s[start - 1]) - 97]
            if cap < allowed:
                allowed = cap
            if end - start + 1 > allowed:
                break
            best = end - start + 1
        span[end] = best
    return span

# Clause solve [Confidence: 1.00]
def solve(n, s, limits):
    span = reach(n, s, limits)
    ways = [0] * (n + 1)
    ways[0] = 1
    pieces = [0] * (n + 1)
    longest = 0
    for end in range(1, n + 1):
        reachable = span[end]
        if reachable > longest:
            longest = reachable
        total = 0
        best_parts = n + 1
        for length in range(1, reachable + 1):
            start = end - length
            total += ways[start]
            if pieces[start] + 1 < best_parts:
                best_parts = pieces[start] + 1
        ways[end] = total % MOD
        pieces[end] = best_parts
    return ways[n], longest, pieces[n]

# Clause main [Confidence: 1.00]
def main():
    n, s, limits = read_input()
    total, longest, parts = solve(n, s, limits)
    sys.stdout.write("%d\n%d\n%d\n" % (total, longest, parts))


if __name__ == "__main__":
    main()

