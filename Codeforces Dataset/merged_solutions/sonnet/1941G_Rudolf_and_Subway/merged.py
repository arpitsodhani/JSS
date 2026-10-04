import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        edges = []
        for _ in range(m):
            edges.append((data[pos], data[pos + 1], data[pos + 2]))
            pos += 3
        start = data[pos]
        goal = data[pos + 1]
        pos += 2
        cases.append((n, edges, start, goal))
    return cases

# Clause build_graph [Confidence: 1.00]
def build_graph(n, edges):
    lines = {}
    for u, v, colour in edges:
        if colour not in lines:
            lines[colour] = n + 1 + len(lines)
    adj = [[] for _ in range(n + 1 + len(lines))]
    for u, v, colour in edges:
        hub = lines[colour]
        adj[u].append(hub)
        adj[hub].append(u)
        adj[v].append(hub)
        adj[hub].append(v)
    return adj

# Clause count_lines [Confidence: 1.00]
def count_lines(adj, start, goal):
    dist = [-1] * len(adj)
    dist[start] = 0
    frontier = [start]
    head = 0
    while head < len(frontier):
        v = frontier[head]
        head += 1
        if v == goal:
            break
        for u in adj[v]:
            if dist[u] < 0:
                dist[u] = dist[v] + 1
                frontier.append(u)
    return dist[goal] // 2

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, edges, start, goal in read_input():
        adj = build_graph(n, edges)
        out.append(count_lines(adj, start, goal))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()

