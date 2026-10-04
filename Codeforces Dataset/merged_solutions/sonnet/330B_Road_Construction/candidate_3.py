import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    pairs = []
    pos = 2
    while len(pairs) < m:
        pairs.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    return n, m, pairs


# --- clause: pick_center :: (n: int, pairs: list[tuple[int, int]]) -> int ---
def pick_center(n, pairs):
    blocked = [False] * (n + 1)
    for a, b in pairs:
        blocked[a] = True
        blocked[b] = True
    city = 1
    while city <= n:
        if not blocked[city]:
            return city
        city += 1
    return 1


# --- clause: build_roads :: (n: int, center: int) -> list[tuple[int, int]] ---
def build_roads(n, center):
    roads = []
    for city in range(n, 0, -1):
        if city != center:
            roads.append((center, city))
    return roads


# --- clause: main :: () -> None ---
def main():
    n, m, pairs = read_input()
    center = pick_center(n, pairs)
    roads = build_roads(n, center)
    out = [str(len(roads))]
    for a, b in roads:
        out.append(str(a) + " " + str(b))
    print("\n".join(out))


if __name__ == "__main__":
    main()
