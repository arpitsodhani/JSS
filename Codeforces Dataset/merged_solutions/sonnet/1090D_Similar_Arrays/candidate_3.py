import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    pairs = []
    for i in range(m):
        pairs.append((fields[2 + 2 * i], fields[3 + 2 * i]))
    return n, pairs


# --- clause: pick_twin :: (n: int, pairs: list[tuple[int, int]]) -> tuple[int, int] | None ---
def pick_twin(n, pairs):
    if n < 2:
        return None
    degree = [0] * (n + 1)
    for a, b in pairs:
        degree[a] += 1
        degree[b] += 1
    peak = 1
    for v in range(2, n + 1):
        if degree[v] < degree[peak]:
            peak = v
    if degree[peak] >= n - 1:
        return None
    linked = set()
    for a, b in pairs:
        if a == peak:
            linked.add(b)
        elif b == peak:
            linked.add(a)
    for v in range(1, n + 1):
        if v != peak and v not in linked:
            return peak, v
    return None


# --- clause: build_arrays :: (n: int, twin: tuple[int, int]) -> tuple[list[int], list[int]] ---
def build_arrays(n, twin):
    u, v = twin
    first = [0] * (n + 1)
    first[u] = 1
    first[v] = 2
    value = 3
    for spot in range(1, n + 1):
        if spot != u and spot != v:
            first[spot] = value
            value += 1
    follow = list(first)
    follow[v] = 1
    return first[1:], follow[1:]


# --- clause: main :: () -> None ---
def main():
    n, pairs = read_input()
    twin = pick_twin(n, pairs)
    if twin is None:
        sys.stdout.write("NO\n")
        return
    first, follow = build_arrays(n, twin)
    sys.stdout.write("YES\n%s\n%s\n" % (" ".join(map(str, first)), " ".join(map(str, follow))))


if __name__ == "__main__":
    main()
