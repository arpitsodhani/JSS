import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode(), data[1].decode()

# Clause last_ends [Confidence: 1.00]
def last_ends(s, t):
    n = len(s)
    length_of = len(t)
    joined = t + "#" + s
    fail = [0] * len(joined)
    for i in range(1, len(joined)):
        delta = fail[i - 1]
        while delta and joined[i] != joined[delta]:
            delta = fail[delta - 1]
        if joined[i] == joined[delta]:
            delta += 1
        fail[i] = delta
    ends = [0] * (n + 1)
    last = 0
    for i in range(n):
        spot = length_of + 1 + i
        if fail[spot] == length_of:
            last = i + 1
        ends[i + 1] = last
    return ends

# Clause count_ways [Confidence: 1.00]
def count_ways(s, t, ends):
    mod = 1000000007
    n = len(s)
    length_of = len(t)
    dp = [0] * (n + 1)
    prefix = [0] * (n + 2)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        stop = ends[i]
        if stop >= length_of:
            reach = stop - length_of
            dp[i] = (dp[i] + prefix[reach] + reach + 1) % mod
        prefix[i] = (prefix[i - 1] + dp[i]) % mod
    return dp[n] % mod

# Clause main [Confidence: 1.00]
def main():
    s, t = read_input()
    sys.stdout.write("%d\n" % count_ways(s, t, last_ends(s, t)))


if __name__ == "__main__":
    main()

