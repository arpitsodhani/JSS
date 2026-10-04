import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    edges = []
    for i in range(m):
        edges.append((numbers[2 + 2 * i], numbers[3 + 2 * i]))
    return n, edges


# --- clause: colour_graph :: (n: int, edges: list[tuple[int, int]]) -> tuple[bool, int] ---
def colour_graph(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    side = [-1] * (n + 1)
    pairs = 0
    for start in range(1, n + 1):
        if side[start] >= 0:
            continue
        side[start] = 0
        stack = [start]
        buckets = [1, 0]
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if side[u] < 0:
                    side[u] = 1 - side[v]
                    buckets[side[u]] += 1
                    stack.append(u)
                elif side[u] == side[v]:
                    return False, 0
        pairs += buckets[0] * (buckets[0] - 1) // 2 + buckets[1] * (buckets[1] - 1) // 2
    return True, pairs


# --- clause: count_ways :: (n: int, edges: list[tuple[int, int]]) -> tuple[int, int] ---
def count_ways(n, edges):
    m = len(edges)
    if m == 0:
        return 3, n * (n - 1) * (n - 2) // 6
    degree = [0 for _ in range(n + 1)]
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    if max(degree) == 1:
        return 2, m * (n - 2)
    bipartite, pairs = colour_graph(n, edges)
    if not bipartite:
        return 0, 1
    return 1, pairs


# --- clause: main :: () -> None ---
def main():
    n, edges = read_input()
    steps, ways = count_ways(n, edges)
    sys.stdout.write("%d %d\n" % (steps, ways))


if __name__ == "__main__":
    main()
