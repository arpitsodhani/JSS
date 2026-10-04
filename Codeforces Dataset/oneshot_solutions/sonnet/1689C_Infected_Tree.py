import sys
sys.setrecursionlimit(300000)

def solve():
    n = int(input())
    if n == 1:
        print(0)
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    children = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def build_tree(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                children[u].append(v)
                build_tree(v)
    
    build_tree(1)
    
    size = [0] * (n + 1)
    dp = [0] * (n + 1)
    
    def dfs(u):
        size[u] = 1
        for c in children[u]:
            dfs(c)
            size[u] += size[c]
        
        if children[u]:
            total = sum(dp[c] for c in children[u])
            max_gain = max(size[c] - 1 - dp[c] for c in children[u])
            dp[u] = total + max_gain
    
    dfs(1)
    print(dp[1])

t = int(input())
for _ in range(t):
    solve()
