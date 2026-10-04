import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, int, int]], list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    m = tokens[1]
    k = tokens[2]
    roads = []
    at = 3
    for _ in range(m):
        roads.append((tokens[at], tokens[at + 1], tokens[at + 2]))
        at += 3
    return roads, tokens[at:at + k]


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
