from collections import deque

def main():
    n, m = map(int, input().split())
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Check if graph is bipartite (no odd cycles)
    color = [-1] * (n + 1)
    is_bipartite = True
    
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break
    
    if not is_bipartite:
        print(0, 1)
        return
    
    # t=1: two non-adjacent vertices with common neighbor
    count = 0
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if v not in adj[u] and len(adj[u] & adj[v]) > 0:
                count += 1
    
    if count > 0:
        print(1, count)
        return
    
    # t=2: edge (u,v) + vertex w not adjacent to both
    if m > 0:
        count = 0
        for u, v in edges:
            for w in range(1, n + 1):
                if w != u and w != v and w not in adj[u] and w not in adj[v]:
                    count += 1
        print(2, count)
        return
    
    # t=3: no edges, form triangle from scratch
    count = n * (n - 1) * (n - 2) // 6
    print(3, count)

main()
