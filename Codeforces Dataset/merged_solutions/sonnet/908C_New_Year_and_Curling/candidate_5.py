import math
import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    r = raw[1]
    return r, raw[2:2 + n]


# --- clause: resting_heights :: (r: int, spots: list[int]) -> list[float] ---
def resting_heights(r, spots):
    heights = []
    for i in range(0, len(spots)):
        champion = float(r)
        for j in range(i):
            gap = spots[i] - spots[j]
            if gap < 0:
                gap = -gap
            if gap > 2 * r:
                continue
            reach = heights[j] + math.sqrt(4.0 * r * r - gap * gap)
            if reach > champion:
                champion = reach
        heights.append(champion)
    return heights


# --- clause: main :: () -> None ---
def main():
    r, spots = read_input()
    heights = resting_heights(r, spots)
    sys.stdout.write(" ".join("%.10f" % item for item in heights) + "\n")


if __name__ == "__main__":
    main()
