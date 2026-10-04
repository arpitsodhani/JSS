import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int], list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    d = data[2]
    affected = data[3:3 + m]
    adj = [[] for _ in range(n + 1)]
    pos = 3 + m
    for _ in range(n - 1):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, m, d, affected, adj


# --- clause: distances :: (n: int, adj: list[list[int]], source: int) -> list[int] ---
def distances(n, adj, source):
    dist = [-1] * (n + 1)
    dist[source] = 0
    frontier = [source]
    depth = 0
    while frontier:
        depth += 1
        nxt = []
        for node in frontier:
            for other in adj[node]:
                if dist[other] < 0:
                    dist[other] = depth
                    nxt.append(other)
        frontier = nxt
    return dist


# --- clause: count_places :: (n: int, m: int, d: int, affected: list[int], adj: list[list[int]]) -> int ---
def count_places(n, m, d, affected, adj):
    if m == 0:
        return n
    first = distances(n, adj, affected[0])
    far = affected[0]
    for node in affected:
        if first[node] > first[far]:
            far = node
    from_far = distances(n, adj, far)
    other = far
    for node in affected:
        if from_far[node] > from_far[other]:
            other = node
    from_other = distances(n, adj, other)
    total = 0
    for node in range(1, n + 1):
        if from_far[node] <= d and from_other[node] <= d:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, m, d, affected, adj = read_input()
    sys.stdout.write(str(count_places(n, m, d, affected, adj)) + "\n")


if __name__ == "__main__":
    main()
