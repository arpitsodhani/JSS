import sys
sys.setrecursionlimit(300000)

n, k = map(int, input().split())

if n == 1:
    print(0)
    print(1)
else:
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # DP: dp[v][(size, has_k_flag)] = max_edges_kept
    dp = [dict() for _ in range(n + 1)]
    
    def dfs(v, parent):
        dp[v][(1, 0)] = 0  # Start with just node v
        
        for u in adj[v]:
            if u == parent:
                continue
            
            dfs(u, v)
            
            new_dp = {}
            for (s1, f1), val1 in dp[v].items():
                for (s2, f2), val2 in dp[u].items():
                    # Option 1: Cut edge to u
                    new_f = f1 | f2 | (1 if s2 == k else 0)
                    key = (s1, new_f)
                    new_dp[key] = max(new_dp.get(key, -1), val1 + val2)
                    
                    # Option 2: Keep edge to u  
                    new_s = s1 + s2
                    new_f = f1 | f2
                    key = (new_s, new_f)
                    new_dp[key] = max(new_dp.get(key, -1), val1 + val2 + 1)
            
            dp[v] = new_dp
    
    dfs(1, -1)
    
    # Find best: either root's component has size k, or has_k flag is set
    best = max(val for (s, f), val in dp[1].items() if f == 1 or s == k)
    print(n - 1 - best)
    
    # Find any k-sized subtree to output
    size = [0] * (n + 1)
    
    def compute_size(v, parent):
        size[v] = 1
        for u in adj[v]:
            if u != parent:
                size[v] += compute_size(u, v)
        return size[v]
    
    compute_size(1, -1)
    
    def find_k_subtree(v, parent):
        if size[v] == k:
            nodes = []
            def collect(u, p):
                nodes.append(u)
                for w in adj[u]:
                    if w != p:
                        collect(w, u)
            collect(v, parent)
            return nodes
        
        for u in adj[v]:
            if u != parent:
                result = find_k_subtree(u, v)
                if result:
                    return result
        return None
    
    k_nodes = find_k_subtree(1, -1)
    print(' '.join(map(str, k_nodes)))
