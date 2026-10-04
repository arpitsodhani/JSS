import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    graph = [[] for _ in range(n)]
    for v in range(1, n):
        p = data[idx] - 1
        idx += 1
        graph[v].append(p)
        graph[p].append(v)
    
    q = data[idx]
    idx += 1
    queries = data[idx:idx + q]
    
    if n == 1:
        print(' '.join(['0'] * q))
        return
    
    degree = [len(graph[i]) for i in range(n)]
    leaf_dist = [-1] * n
    queue = deque()
    
    for i in range(n):
        if degree[i] == 1:
            leaf_dist[i] = 0
            queue.append(i)
    
    while queue:
        v = queue.popleft()
        for to in graph[v]:
            if leaf_dist[to] == -1:
                leaf_dist[to] = leaf_dist[v] + 1
                queue.append(to)
    
    max_sum = 2 * max(leaf_dist)
    best = [0] * (max_sum + 1)
    diameter = 0
    
    for start in range(n):
        dist = [-1] * n
        dist[start] = 0
        queue = deque([start])
        
        while queue:
            v = queue.popleft()
            for to in graph[v]:
                if dist[to] == -1:
                    dist[to] = dist[v] + 1
                    queue.append(to)
        
        for v in range(start + 1, n):
            d = dist[v]
            s = leaf_dist[start] + leaf_dist[v]
            if d > best[s]:
                best[s] = d
            if d > diameter:
                diameter = d
    
    for s in range(max_sum - 1, -1, -1):
        if best[s + 1] > best[s]:
            best[s] = best[s + 1]
    
    precomputed = [0] * (diameter + 1)
    for x in range(1, diameter + 1):
        ans = 0
        for s in range(max_sum + 1):
            cur = best[s]
            if cur > x + s:
                cur = x + s
            if cur > ans:
                ans = cur
        precomputed[x] = ans
    
    result = []
    for x in queries:
        if x >= diameter:
            result.append(str(diameter))
        else:
            result.append(str(precomputed[x]))
    
    print(' '.join(result))

if __name__ == "__main__":
    main()
