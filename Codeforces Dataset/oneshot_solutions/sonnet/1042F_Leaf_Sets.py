import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    k = data[1]
    
    graph = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(n - 1):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
    
    if n == 1:
        print(1)
        return
    
    root = 1
    for i in range(1, n + 1):
        if len(graph[i]) > 1:
            root = i
            break
    
    parent = [0] * (n + 1)
    order = [root]
    parent[root] = -1
    
    for v in order:
        for to in graph[v]:
            if to != parent[v]:
                parent[to] = v
                order.append(to)
    
    answer = 0
    best = [0] * (n + 1)
    
    for v in reversed(order):
        if v != root and len(graph[v]) == 1:
            best[v] = 0
            continue
        
        distances = []
        for to in graph[v]:
            if parent[to] == v:
                distances.append(best[to] + 1)
        
        if not distances:
            best[v] = 0
            continue
        
        distances.sort()
        while len(distances) >= 2 and distances[-1] + distances[-2] > k:
            answer += 1
            distances.pop()
        
        best[v] = distances[-1]
    
    print(answer + 1)

if __name__ == "__main__":
    main()
