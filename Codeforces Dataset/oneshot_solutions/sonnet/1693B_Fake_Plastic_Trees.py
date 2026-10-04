import sys
sys.setrecursionlimit(300000)

def solve():
    n = int(input())
    
    if n == 1:
        l, r = map(int, input().split())
        print(0 if l == 0 else 1)
        return
    
    parents = [0] + list(map(int, input().split()))
    children = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        children[parents[i]].append(i)
    
    l = [0] * (n + 1)
    r = [0] * (n + 1)
    for i in range(1, n + 1):
        l[i], r[i] = map(int, input().split())
    
    def dfs(v):
        if not children[v]:  # leaf
            if l[v] == 0:
                return (0, 0)
            return (1, r[v])
        
        ops = 0
        total = 0
        for c in children[v]:
            ops_c, leftover_c = dfs(c)
            ops += ops_c
            total += leftover_c
        
        if total < l[v]:
            ops += 1
            leftover = r[v]
        else:
            leftover = min(total, r[v])
        
        return (ops, leftover)
    
    ops, _ = dfs(1)
    print(ops)

t = int(input())
for _ in range(t):
    solve()
