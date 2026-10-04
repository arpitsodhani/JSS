import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    out = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        a = [0] + data[idx:idx + n]
        idx += n
        
        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = data[idx]
            v = data[idx + 1]
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        
        answer = [0] * (n + 1)
        stack = [(1, 0, 0, 0, 0, 0)]
        
        while stack:
            v, parent, depth, prefix_parent, min_prefix, max_prefix = stack.pop()
            
            if depth % 2 == 0:
                prefix = prefix_parent + a[v]
                answer[v] = prefix - min_prefix
            else:
                prefix = prefix_parent - a[v]
                answer[v] = max_prefix - prefix
            
            new_min = min(min_prefix, prefix)
            new_max = max(max_prefix, prefix)
            
            for to in graph[v]:
                if to != parent:
                    stack.append((to, v, depth + 1, prefix, new_min, new_max))
        
        out.append(' '.join(map(str, answer[1:])))
    
    print('\n'.join(out))

solve()
