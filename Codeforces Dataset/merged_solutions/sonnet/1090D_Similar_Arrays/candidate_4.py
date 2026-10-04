import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    pairs = []
    for i in range(m):
        pairs.append((numbers[2 + 2 * i], numbers[3 + 2 * i]))
    return n, pairs


# --- clause: pick_twin :: (n: int, pairs: list[tuple[int, int]]) -> tuple[int, int] | None ---
def pick_twin(n, pairs):
    if n < 2 or len(pairs) >= n * (n - 1) // 2:
        return None
    linked = [set() for _ in range(n + 1)]
    for a, b in pairs:
        linked[a].add(b)
        linked[b].add(a)
    best = 1
    for v in range(2, n + 1):
        if len(linked[v]) < len(linked[best]):
            best = v
    for v in range(1, n + 1):
        if v != best and v not in linked[best]:
            return best, v
    return None


# --- clause: build_arrays :: (n: int, twin: tuple[int, int]) -> tuple[list[int], list[int]] ---
def build_arrays(n, twin):
    u, v = twin
    first = [0 for _ in range(n + 1)]
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
