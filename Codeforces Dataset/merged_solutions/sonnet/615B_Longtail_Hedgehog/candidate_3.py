import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    edges = []
    for i in range(m):
        edges.append((fields[2 + 2 * i], fields[3 + 2 * i]))
    return n, edges


# --- clause: best_beauty :: (n: int, edges: list[tuple[int, int]]) -> int ---
def best_beauty(n, edges):
    lower = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
        if u < v:
            lower[v].append(u)
        else:
            lower[u].append(v)
    tail = [1] * (n + 1)
    peak = 0
    for v in range(1, n + 1):
        for u in lower[v]:
            if tail[u] + 1 > tail[v]:
                tail[v] = tail[u] + 1
        here = tail[v] * degree[v]
        if here > peak:
            peak = here
    return peak


# --- clause: main :: () -> None ---
def main():
    n, edges = read_input()
    sys.stdout.write("%d\n" % best_beauty(n, edges))


if __name__ == "__main__":
    main()
