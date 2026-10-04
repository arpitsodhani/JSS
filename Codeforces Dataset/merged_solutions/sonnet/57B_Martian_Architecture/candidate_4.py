import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, int, int]], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    m = numbers[1]
    k = numbers[2]
    roads = []
    cursor = 3
    for _ in range(m):
        roads.append((numbers[cursor], numbers[cursor + 1], numbers[cursor + 2]))
        cursor += 3
    return roads, numbers[cursor:cursor + k]


# --- clause: total_stones :: (roads: list[tuple[int, int, int]], asked: list[int]) -> int ---
def total_stones(roads, asked):
    total = 0
    for low, high, first in roads:
        for spot in asked:
            if spot < low or spot > high:
                continue
            total += first + (spot - low)
    return total


# --- clause: main :: () -> None ---
def main():
    roads, asked = read_input()
    sys.stdout.write("%d\n" % total_stones(roads, asked))


if __name__ == "__main__":
    main()
