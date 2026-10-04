import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    graph = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    
    for _ in range(n - 1):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    special = data[idx:idx + m]
    is_special = [False] * (n + 1)
    for v in special:
        is_special[v] = True
    
    removed = [False] * (n + 1)
    q = deque()
    
    for v in range(1, n + 1):
        if degree[v] == 1 and not is_special[v]:
            q.append(v)
    
    removed_count = 0
    while q:
        v = q.popleft()
        if removed[v]:
            continue
        
        removed[v] = True
        removed_count += 1
        
        for to in graph[v]:
            if not removed[to]:
                degree[to] -= 1
                if degree[to] == 1 and not is_special[to]:
                    q.append(to)
    
    subtree_edges = n - removed_count - 1
    
    def farthest(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        best = start
        
        while q:
            v = q.popleft()
            if is_special[v]:
                if dist[v] > dist[best] or (dist[v] == dist[best] and v < best):
                    best = v
            
            for to in graph[v]:
                if not removed[to] and dist[to] == -1:
                    dist[to] = dist[v] + 1
                    q.append(to)
        
        return best, dist[best]
    
    a, _ = farthest(special[0])
    b, diameter = farthest(a)
    
    start = min(a, b)
    time = 2 * subtree_edges - diameter
    
    print(start)
    print(time)

if __name__ == "__main__":
    main()
