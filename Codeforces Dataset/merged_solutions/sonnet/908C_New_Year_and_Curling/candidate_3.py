import math
import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    r = fields[1]
    return r, fields[2:2 + n]


# --- clause: resting_heights :: (r: int, spots: list[int]) -> list[float] ---
def resting_heights(r, spots):
    heights = []
    for i in range(len(spots)):
        peak = float(r)
        for j in range(i):
            gap = spots[i] - spots[j]
            if gap < 0:
                gap = -gap
            if gap > 2 * r:
                continue
            reach = heights[j] + math.sqrt(4.0 * r * r - gap * gap)
            if reach > peak:
                peak = reach
        heights.append(peak)
    return heights


# --- clause: main :: () -> None ---
def main():
    r, spots = read_input()
    heights = resting_heights(r, spots)
    sys.stdout.write(" ".join("%.10f" % entry for entry in heights) + "\n")


if __name__ == "__main__":
    main()
