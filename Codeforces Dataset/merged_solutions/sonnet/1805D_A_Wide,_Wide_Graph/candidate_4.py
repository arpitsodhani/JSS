import sys


# --- clause: read_input :: () -> tuple[int, list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    adj = [[] for _ in range(n + 1)]
    pos = 1
    for _ in range(n - 1):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, adj


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


# --- clause: component_counts :: (n: int, adj: list[list[int]]) -> list[int] ---
def component_counts(n, adj):
    probe = distances(n, adj, 1)
    end_a = 1
    for v in range(2, n + 1):
        if probe[v] > probe[end_a]:
            end_a = v
    from_a = distances(n, adj, end_a)
    end_b = end_a
    for v in range(1, n + 1):
        if from_a[v] > from_a[end_b]:
            end_b = v
    from_b = distances(n, adj, end_b)
    tally = [0] * (n + 2)
    for v in range(1, n + 1):
        ecc = from_a[v]
        if from_b[v] > ecc:
            ecc = from_b[v]
        tally[ecc] += 1
    result = []
    alone = 0
    for k in range(1, n + 1):
        alone += tally[k - 1]
        if alone == n:
            result.append(n)
        else:
            result.append(alone + 1)
    return result


# --- clause: main :: () -> None ---
def main():
    n, adj = read_input()
    sys.stdout.write(" ".join(map(str, component_counts(n, adj))) + "\n")


if __name__ == "__main__":
    main()
