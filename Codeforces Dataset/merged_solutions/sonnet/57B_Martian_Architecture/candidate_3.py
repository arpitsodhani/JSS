import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, int, int]], list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    m = fields[1]
    k = fields[2]
    roads = []
    offset = 3
    for _ in range(m):
        roads.append((fields[offset], fields[offset + 1], fields[offset + 2]))
        offset += 3
    return roads, fields[offset:offset + k]


# --- clause: total_stones :: (roads: list[tuple[int, int, int]], asked: list[int]) -> int ---
def total_stones(roads, asked):
    total = 0
    for spot in asked:
        for low, high, lead in roads:
            if low <= spot <= high:
                total += lead + spot - low
    return total


# --- clause: main :: () -> None ---
def main():
    roads, asked = read_input()
    sys.stdout.write("%d\n" % total_stones(roads, asked))


if __name__ == "__main__":
    main()
