import math
import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    r = numbers[1]
    return r, numbers[2:2 + n]


# --- clause: resting_heights :: (r: int, spots: list[int]) -> list[float] ---
def resting_heights(r, spots):
    heights = []
    reach = 4 * r * r
    for i in range(len(spots)):
        best = float(r)
        here = spots[i]
        for j in range(i - 1, -1, -1):
            gap = here - spots[j]
            room = reach - gap * gap
            if room < 0:
                continue
            climb = heights[j] + math.sqrt(room)
            if climb > best:
                best = climb
        heights.append(best)
    return heights


# --- clause: main :: () -> None ---
def main():
    r, spots = read_input()
    heights = resting_heights(r, spots)
    sys.stdout.write(" ".join("%.10f" % value for value in heights) + "\n")


if __name__ == "__main__":
    main()
