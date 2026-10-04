import sys
sys.setrecursionlimit(300000)

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print(0)
        return
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    used_edges = set()
    episodes = []
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        available = []
        
        for v in graph[u]:
            edge = (min(u, v), max(u, v))
            if edge not in used_edges:
                available.append(v)
        
        # Pair up available neighbors
        for i in range(0, len(available) - 1, 2):
            v1, v2 = available[i], available[i + 1]
            episodes.append([v1, u, v2])
            used_edges.add((min(u, v1), max(u, v1)))
            used_edges.add((min(u, v2), max(u, v2)))
        
        # Continue DFS to all unvisited neighbors
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    print(len(episodes))
    for ep in episodes:
        print(*ep)

solve()
