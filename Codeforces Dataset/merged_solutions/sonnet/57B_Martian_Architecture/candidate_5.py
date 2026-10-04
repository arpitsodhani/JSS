import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, int, int]], list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    m = raw[1]
    k = raw[2]
    roads = []
    reader = 3
    for _ in range(m):
        roads.append((raw[reader], raw[reader + 1], raw[reader + 2]))
        reader += 3
    return roads, raw[reader:reader + k]


# --- clause: total_stones :: (roads: list[tuple[int, int, int]], asked: list[int]) -> int ---
def total_stones(roads, asked):
    total = 0
    for spot in asked:
        for floor_value, high, first in roads:
            if floor_value <= spot <= high:
                total += first + spot - floor_value
    return total


# --- clause: main :: () -> None ---
def main():
    roads, asked = read_input()
    sys.stdout.write("%d\n" % total_stones(roads, asked))


if __name__ == "__main__":
    main()
