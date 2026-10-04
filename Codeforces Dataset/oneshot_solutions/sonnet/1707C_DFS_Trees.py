import sys
from collections import defaultdict

sys.setrecursionlimit(300000)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    idx += 2
    
    edges = []
    graph = defaultdict(list)
    
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        graph[u].append((v, i))
        graph[v].append((u, i))
    
    # Sort edges for each vertex by edge index (weight)
    for u in graph:
        graph[u].sort(key=lambda x: x[1])
    
    # Find MST using Kruskal
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    mst_edges = set()
    
    for i in range(m):
        u, v = edges[i]
        if union(parent, rank, u, v):
            mst_edges.add(i)
    
    # For each starting vertex, run DFS
    result = []
    
    for start in range(1, n + 1):
        vis = [False] * (n + 1)
        dfs_edges = set()
        
        def dfs(u):
            vis[u] = True
            for v, edge_idx in graph[u]:
                if not vis[v]:
                    dfs_edges.add(edge_idx)
                    dfs(v)
        
        dfs(start)
        
        if dfs_edges == mst_edges:
            result.append('1')
        else:
            result.append('0')
    
    print(''.join(result))

if __name__ == '__main__':
    main()
