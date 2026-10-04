import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    pairs = []
    idx = 2
    for _ in range(m):
        first, second = int(data[idx]), int(data[idx + 1])
        idx += 2
        pairs.append((first, second))
    return n, m, pairs


# --- clause: pick_center :: (n: int, pairs: list[tuple[int, int]]) -> int ---
def pick_center(n, pairs):
    blocked = [False] * (n + 1)
    for first, second in pairs:
        blocked[first] = True
        blocked[second] = True
    for city in range(1, n + 1):
        if blocked[city]:
            continue
        return city
    return 1


# --- clause: build_roads :: (n: int, center: int) -> list[tuple[int, int]] ---
def build_roads(n, center):
    roads = []
    for city in range(1, n + 1):
        if city == center:
            continue
        roads.append((center, city))
    return roads


# --- clause: main :: () -> None ---
def main():
    n, m, pairs = read_input()
    hub = pick_center(n, pairs)
    roads = build_roads(n, hub)
    lines = [str(len(roads))]
    for first, second in roads:
        lines.append("%d %d" % (first, second))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
