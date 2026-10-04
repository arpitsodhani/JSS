import sys

# Clause read_input [Confidence: 1.00]
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

# Clause distances_by_kind [Confidence: 1.00]
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

# Clause cheapest_fairs [Confidence: 1.00]
def cheapest_fairs(n, k, s, table):
    answer = [0] * n
    for node, costs in enumerate(zip(*table)):
        answer[node] = sum(sorted(costs)[:s])
    return answer

# Clause main [Confidence: 0.60]
def main():
    n, m, k, s, kinds, adj = read_input()
    table = distances_by_kind(n, k, kinds, adj)
    sys.stdout.write(" ".join(map(str, cheapest_fairs(n, k, s, table))) + "\n")


if __name__ == "__main__":
    main()

