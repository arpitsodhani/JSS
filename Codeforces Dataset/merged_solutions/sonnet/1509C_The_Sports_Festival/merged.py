import sys

# Clause read_input [Confidence: 0.60]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    speeds = [int(token) for token in data[1:n + 1]]
    return n, speeds

# Clause smallest_sum [Confidence: 1.00]
def smallest_sum(n, speeds):
    speeds.sort()
    if n == 1:
        return 0
    prev = [0] * n
    for width in range(1, n):
        m = n - width
        lefts = prev[1:]
        rights = prev[:m]
        sj = speeds[width:]
        si = speeds[:m]
        prev = [b - a + (l if l < r else r) for a, b, l, r in zip(si, sj, lefts, rights)]
    return prev[0]

# Clause main [Confidence: 0.40]
def main():
    n, speeds = read_input()
    sys.stdout.write(str(smallest_sum(n, speeds)) + "\n")


if __name__ == "__main__":
    main()

