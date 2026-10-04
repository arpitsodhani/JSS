import sys
sys.setrecursionlimit(200000)

def solve():
    n, m, d = map(int, sys.stdin.readline().split())
    affected = set(map(int, sys.stdin.readline().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    down = [-1] * (n + 1)
    
    def dfs1(u, parent):
        if u in affected:
            down[u] = 0
        
        for v in adj[u]:
            if v != parent:
                dfs1(v, u)
                if down[v] != -1:
                    down[u] = max(down[u], down[v] + 1)
    
    up = [-1] * (n + 1)
    
    def dfs2(u, parent):
        children = [v for v in adj[u] if v != parent]
        
        for child in children:
            max_val = -1
            
            if up[u] != -1:
                max_val = max(max_val, up[u] + 1)
            
            if u in affected:
                max_val = max(max_val, 1)
            
            for sibling in children:
                if sibling != child and down[sibling] != -1:
                    max_val = max(max_val, down[sibling] + 2)
            
            up[child] = max_val
        
        for child in children:
            dfs2(child, u)
    
    dfs1(1, -1)
    up[1] = -1
    dfs2(1, -1)
    
    count = 0
    for u in range(1, n + 1):
        max_dist = max(down[u], up[u])
        if max_dist != -1 and max_dist <= d:
            count += 1
    
    print(count)

solve()
