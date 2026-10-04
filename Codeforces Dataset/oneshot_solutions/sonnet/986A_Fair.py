import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    k = int(input_data[idx + 2])
    s = int(input_data[idx + 3])
    idx += 4
    
    goods = [0] * (n + 1)
    for i in range(1, n + 1):
        goods[i] = int(input_data[idx])
        idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    INF = n + 1
    dist_to_good = [[INF] * (k + 1) for _ in range(n + 1)]
    
    for good in range(1, k + 1):
        queue = deque()
        visited = [False] * (n + 1)
        
        for town in range(1, n + 1):
            if goods[town] == good:
                queue.append(town)
                visited[town] = True
                dist_to_good[town][good] = 0
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    dist_to_good[v][good] = dist_to_good[u][good] + 1
                    queue.append(v)
    
    result = []
    for town in range(1, n + 1):
        distances = [dist_to_good[town][good] for good in range(1, k + 1)]
        distances.sort()
        result.append(sum(distances[:s]))
    
    print(' '.join(map(str, result)))

solve()
