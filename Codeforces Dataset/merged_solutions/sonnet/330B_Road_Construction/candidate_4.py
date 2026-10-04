import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    pairs = []
    for i in range(m):
        a = int(data[2 + 2 * i])
        b = int(data[3 + 2 * i])
        pairs.append((a, b))
    return n, m, pairs


# --- clause: pick_center :: (n: int, pairs: list[tuple[int, int]]) -> int ---
def pick_center(n, pairs):
    blocked = [False] * (n + 1)
    for pair in pairs:
        blocked[pair[0]] = True
        blocked[pair[1]] = True
    for city in range(1, n + 1):
        if not blocked[city]:
            return city
    return 1


# --- clause: build_roads :: (n: int, center: int) -> list[tuple[int, int]] ---
def build_roads(n, center):
    roads = []
    for city in range(1, n + 1):
        if city != center:
            roads.append((center, city))
    return roads


# --- clause: main :: () -> None ---
def main():
    n, m, pairs = read_input()
    center = pick_center(n, pairs)
    roads = build_roads(n, center)
    out = [str(len(roads))]
    for road in roads:
        out.append(str(road[0]) + " " + str(road[1]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
