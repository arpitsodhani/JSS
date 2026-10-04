import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, list[int], list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    k = data[2]
    s = data[3]
    kinds = data[4:4 + n]
    adj = [[] for _ in range(n)]
    pos = 4 + n
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, m, k, s, kinds, adj

# --- clause: distances_by_kind :: (n: int, k: int, kinds: list[int], adj: list[list[int]]) -> list[list[int]] ---
def distances_by_kind(n, k, kinds, adj):
    adj_fast = tuple(tuple(row) for row in adj)
    sources = [[] for _ in range(k + 1)]
    for node, kind in enumerate(kinds):
        sources[kind].append(node)
    table = []
    for kind in range(1, k + 1):
        dist = [-1] * n
        queue = sources[kind][:]
        for node in queue:
            dist[node] = 0
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            step = dist[u] + 1
            for w in adj_fast[u]:
                if dist[w] < 0:
                    dist[w] = step
                    queue.append(w)
        table.append(dist)
    return table


# --- clause: cheapest_fairs :: (n: int, k: int, s: int, table: list[list[int]]) -> list[int] ---
def cheapest_fairs(n, k, s, table):
    answer = [0] * n
    for node, costs in enumerate(zip(*table)):
        answer[node] = sum(sorted(costs)[:s])
    return answer


# --- clause: main :: () -> None ---
def main():
    n, m, k, s, kinds, adj = read_input()
    table = distances_by_kind(n, k, kinds, adj)
    answer = cheapest_fairs(n, k, s, table)
    sys.stdout.write(" ".join(str(v) for v in answer) + "\n")


if __name__ == "__main__":
    main()
