import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause destroy_steps [Confidence: 1.00]
def destroy_steps(h):
    n = len(h)
    left = [0] * n
    left[0] = 1 if h[0] else 0
    for i in range(1, n):
        step = left[i - 1] + 1
        left[i] = step if step < h[i] else h[i]
    best = 0
    high = 0
    for i in range(n - 1, -1, -1):
        step = high + 1
        high = step if step < h[i] else h[i]
        here = high if high < left[i] else left[i]
        if here > best:
            best = here
    return best

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % destroy_steps(read_input()))


if __name__ == "__main__":
    main()

