import sys
from collections import deque

def max_flow_bfs(adj, source, sink, n_nodes):
    def bfs():
        parent = [-1] * n_nodes
        visited = [False] * n_nodes
        visited[source] = True
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            for i in range(len(adj[u])):
                v, cap, _ = adj[u][i]
                if not visited[v] and cap > 0:
                    visited[v] = True
                    parent[v] = (u, i)
                    queue.append(v)
                    if v == sink:
                        return parent
        return parent
    
    max_flow = 0
    while True:
        parent = bfs()
        if parent[sink] == -1:
            break
        
        path_flow = float('inf')
        v = sink
        while v != source:
            u, edge_idx = parent[v]
            path_flow = min(path_flow, adj[u][edge_idx][1])
            v = u
        
        v = sink
        while v != source:
            u, edge_idx = parent[v]
            adj[u][edge_idx][1] -= path_flow
            rev_idx = adj[u][edge_idx][2]
            adj[v][rev_idx][1] += path_flow
            v = u
        
        max_flow += path_flow
    
    return max_flow

def solve():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        
        count = [0] * 10
        for c in s:
            count[int(c)] += 1
        
        valid_times = []
        for hh in range(12):
            for mm in range(60):
                time_str = f"{hh:02d}{mm:02d}"
                valid_times.append(time_str)
        
        source = 0
        sink = 731
        n_nodes = 732
        
        adj = [[] for _ in range(n_nodes)]
        
        def add_edge(u, v, cap):
            adj[u].append([v, cap, len(adj[v])])
            adj[v].append([u, 0, len(adj[u]) - 1])
        
        time_offset = 1
        digit_offset = 721
        
        for i in range(len(valid_times)):
            add_edge(source, time_offset + i, n)
        
        for i, time_str in enumerate(valid_times):
            digit_count = [0] * 10
            for c in time_str:
                digit_count[int(c)] += 1
            for d in range(10):
                if digit_count[d] > 0:
                    add_edge(time_offset + i, digit_offset + d, n)
        
        for d in range(10):
            add_edge(digit_offset + d, sink, count[d])
        
        flow = max_flow_bfs(adj, source, sink, n_nodes)
        print(flow // 4)

solve()
