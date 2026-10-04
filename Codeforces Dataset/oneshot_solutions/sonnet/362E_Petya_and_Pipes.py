from collections import deque

def solve():
    n, k = map(int, input().split())
    adj = []
    for i in range(n):
        row = list(map(int, input().split()))
        adj.append(row)
    
    # Layered graph: layer 0 (nodes 0..n-1), layer 1 (nodes n..2n-1)
    # X_in, X_out for transition bottleneck, T for super-sink
    X_in = 2 * n
    X_out = 2 * n + 1
    T = 2 * n + 2
    total_nodes = 2 * n + 3
    
    graph = [[] for _ in range(total_nodes)]
    
    def add_edge(u, v, cap):
        graph[u].append([v, cap, len(graph[v])])
        graph[v].append([u, 0, len(graph[u]) - 1])
    
    INF = 10**9
    
    # Add edges in both layers
    for u in range(n):
        for v in range(n):
            if adj[u][v] > 0:
                add_edge(u, v, adj[u][v])  # Layer 0: original capacity
                add_edge(u + n, v + n, INF)  # Layer 1: infinite capacity
    
    # Transition between layers through bottleneck
    for i in range(n):
        add_edge(i, X_in, INF)
        add_edge(X_out, i + n, INF)
    
    add_edge(X_in, X_out, k)  # Bottleneck with capacity k
    
    # Connect both layer sinks to super-sink
    add_edge(n - 1, T, INF)
    add_edge(2 * n - 1, T, INF)
    
    # Dinic's algorithm for max flow
    def bfs(source, sink):
        level = [-1] * total_nodes
        level[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v, cap, _ in graph[u]:
                if level[v] < 0 and cap > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return level
    
    def dfs(u, sink, flow, level, iter):
        if u == sink:
            return flow
        while iter[u] < len(graph[u]):
            v, cap, rev = graph[u][iter[u]]
            if level[v] > level[u] and cap > 0:
                d = dfs(v, sink, min(flow, cap), level, iter)
                if d > 0:
                    graph[u][iter[u]][1] -= d
                    graph[v][rev][1] += d
                    return d
            iter[u] += 1
        return 0
    
    source = 0  # Node 1 is 0-indexed as node 0
    max_flow = 0
    while True:
        level = bfs(source, T)
        if level[T] < 0:
            break
        iter = [0] * total_nodes
        while True:
            f = dfs(source, T, INF, level, iter)
            if f == 0:
                break
            max_flow += f
    
    print(max_flow)

solve()
