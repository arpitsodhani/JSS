import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, int, int]], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    m = data[1]
    k = data[2]
    roads = []
    pos = 3
    for _ in range(m):
        roads.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return roads, data[pos:pos + k]


# --- clause: total_stones :: (roads: list[tuple[int, int, int]], asked: list[int]) -> int ---
def total_stones(roads, asked):
    total = 0
    for spot in asked:
        for low, high, first in roads:
            if low <= spot <= high:
                total += first + spot - low
    return total


# --- clause: main :: () -> None ---
def main():
    roads, asked = read_input()
    sys.stdout.write("%d\n" % total_stones(roads, asked))


if __name__ == "__main__":
    main()
