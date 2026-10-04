import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause block_count [Confidence: 0.80]
def block_count(h):
    n = len(h)
    tail = [0] * (n + 1)
    tail[n] = 1 << 62
    for i in range(n - 1, -1, -1):
        tail[i] = h[i] if h[i] < tail[i + 1] else tail[i + 1]
    blocks = 0
    peak = -1
    for i in range(n):
        if h[i] > peak:
            peak = h[i]
        if peak <= tail[i + 1]:
            blocks += 1
    return blocks

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % block_count(read_input()))


if __name__ == "__main__":
    main()

