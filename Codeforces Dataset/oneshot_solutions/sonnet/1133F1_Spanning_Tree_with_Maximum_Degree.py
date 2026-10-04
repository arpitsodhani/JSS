import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    idx += 2
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    # Find vertex with maximum degree
    max_deg = -1
    root = 1
    for i in range(1, n + 1):
        if len(adj[i]) > max_deg:
            max_deg = len(adj[i])
            root = i
    
    # BFS from root to build spanning tree
    visited = [False] * (n + 1)
    queue = deque([root])
    visited[root] = True
    edges = []
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                edges.append((u, v))
    
    # Output edges
    for u, v in edges:
        print(u, v)

if __name__ == "__main__":
    main()
