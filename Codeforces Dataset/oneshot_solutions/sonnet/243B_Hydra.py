import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    n = data[idx]
    m = data[idx + 1]
    h = data[idx + 2]
    t = data[idx + 3]
    idx += 4
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    if h == 0 and t == 0:
        u, v = edges[0]
        print("YES")
        print(u, v)
        print()
        print()
        return
    
    mark = [0] * (n + 1)
    timer = 0
    
    def try_edge(u, v):
        nonlocal timer
        
        if len(adj[u]) - 1 < h or len(adj[v]) - 1 < t:
            return None
        if len(adj[u]) + len(adj[v]) - 2 < h + t:
            return None
        
        timer += 2
        own_mark = timer
        common_mark = timer + 1
        
        for x in adj[u]:
            if x != v:
                mark[x] = own_mark
        
        tail_only = []
        common = []
        
        for x in adj[v]:
            if x == u:
                continue
            if mark[x] == own_mark:
                mark[x] = common_mark
                common.append(x)
            else:
                tail_only.append(x)
        
        head_only = []
        for x in adj[u]:
            if x != v and mark[x] == own_mark:
                head_only.append(x)
        
        need_heads = max(0, h - len(head_only))
        need_tails = max(0, t - len(tail_only))
        
        if need_heads + need_tails > len(common):
            return None
        
        heads = head_only[:h] + common[:need_heads]
        tails = tail_only[:t] + common[need_heads:need_heads + need_tails]
        
        return heads, tails
    
    for u, v in edges:
        result = try_edge(u, v)
        if result is not None:
            heads, tails = result
            print("YES")
            print(u, v)
            print(" ".join(map(str, heads)))
            print(" ".join(map(str, tails)))
            return
        
        result = try_edge(v, u)
        if result is not None:
            heads, tails = result
            print("YES")
            print(v, u)
            print(" ".join(map(str, heads)))
            print(" ".join(map(str, tails)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()
