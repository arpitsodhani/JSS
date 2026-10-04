import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    pairs = []
    for i in range(m):
        pairs.append((data[2 + 2 * i], data[3 + 2 * i]))
    return n, pairs


# --- clause: pick_twin :: (n: int, pairs: list[tuple[int, int]]) -> tuple[int, int] | None ---
def pick_twin(n, pairs):
    if n < 2:
        return None
    degree = [0] * (n + 1)
    for a, b in pairs:
        degree[a] += 1
        degree[b] += 1
    best = 1
    for v in range(2, n + 1):
        if degree[v] < degree[best]:
            best = v
    if degree[best] >= n - 1:
        return None
    linked = set()
    for a, b in pairs:
        if a == best:
            linked.add(b)
        elif b == best:
            linked.add(a)
    for v in range(1, n + 1):
        if v != best and v not in linked:
            return best, v
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
    second = list(first)
    second[v] = 1
    return first[1:], second[1:]


# --- clause: main :: () -> None ---
def main():
    n, pairs = read_input()
    twin = pick_twin(n, pairs)
    if twin is None:
        sys.stdout.write("NO\n")
        return
    first, second = build_arrays(n, twin)
    sys.stdout.write("YES\n%s\n%s\n" % (" ".join(map(str, first)), " ".join(map(str, second))))


if __name__ == "__main__":
    main()
