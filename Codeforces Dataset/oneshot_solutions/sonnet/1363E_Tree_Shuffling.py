import sys

sys.setrecursionlimit(200005)

def solve():
    input = sys.stdin.readline
    n = int(input())
    
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    
    for i in range(1, n + 1):
        ai, bi, ci = map(int, input().split())
        a[i] = ai
        b[i] = bi
        c[i] = ci
    
    # Check if transformation is possible
    if sum(b) != sum(c):
        print(-1)
        return
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Root the tree at node 1
    children = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    def root_tree(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                children[u].append(v)
                root_tree(v)
    
    root_tree(1)
    
    # Top-down DFS: compute min_cost_to_root
    min_cost_to_root = [0] * (n + 1)
    
    def top_down(u, min_cost):
        min_cost_to_root[u] = min(min_cost, a[u])
        for v in children[u]:
            top_down(v, min_cost_to_root[u])
    
    top_down(1, 10**18)
    
    # Bottom-up DFS: compute cost
    total_cost = [0]
    
    def bottom_up(u):
        # Count nodes needing 0→1 and 1→0 in subtree
        cnt0 = 1 if (b[u] == 0 and c[u] == 1) else 0
        cnt1 = 1 if (b[u] == 1 and c[u] == 0) else 0
        
        for v in children[u]:
            c0, c1 = bottom_up(v)
            cnt0 += c0
            cnt1 += c1
        
        # Fix pairs if this is the minimum cost node on path to root
        if a[u] == min_cost_to_root[u]:
            pairs = min(cnt0, cnt1)
            if pairs > 0:
                total_cost[0] += 2 * pairs * a[u]
                cnt0 -= pairs
                cnt1 -= pairs
        
        return cnt0, cnt1
    
    bottom_up(1)
    
    print(total_cost[0])

solve()
