import sys
from bisect import bisect_right

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    q = data[1]
    a = data[2:2 + n]
    shots = data[2 + n:2 + n + q]
    return n, q, a, shots

# Clause standing_counts [Confidence: 1.00]
def standing_counts(n, a, shots):
    prefix = []
    running = 0
    for value in a:
        running += value
        prefix.append(running)
    total = running
    out = []
    fired = 0
    for arrows in shots:
        fired += arrows
        if fired >= total:
            fired = 0
            out.append(n)
        else:
            out.append(n - bisect_right(prefix, fired))
    return out

# Clause main [Confidence: 1.00]
def main():
    n, q, a, shots = read_input()
    sys.stdout.write("\n".join(map(str, standing_counts(n, a, shots))) + "\n")


if __name__ == "__main__":
    main()

