import math
import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    r = data[1]
    return r, data[2:2 + n]

# Clause resting_heights [Confidence: 1.00]
def resting_heights(r, spots):
    heights = []
    for i in range(len(spots)):
        best = float(r)
        for j in range(i):
            gap = spots[i] - spots[j]
            if gap < 0:
                gap = -gap
            if gap > 2 * r:
                continue
            reach = heights[j] + math.sqrt(4.0 * r * r - gap * gap)
            if reach > best:
                best = reach
        heights.append(best)
    return heights

# Clause main [Confidence: 1.00]
def main():
    r, spots = read_input()
    heights = resting_heights(r, spots)
    sys.stdout.write(" ".join("%.10f" % entry for entry in heights) + "\n")


if __name__ == "__main__":
    main()

