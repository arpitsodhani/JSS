import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    k = int(data[idx + 2])
    idx += 3
    
    # Build friendship graph
    friends = [set() for _ in range(n + 1)]
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        if a != b:
            friends[a].add(b)
            friends[b].add(a)
    
    # Build dislike set
    dislikes = set()
    for _ in range(k):
        a = int(data[idx])
        b = int(data[idx + 1])
        idx += 2
        if a != b:
            dislikes.add((min(a, b), max(a, b)))
    
    # Find connected components and check validity
    visited = [False] * (n + 1)
    max_size = 0
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
        
        # BFS to find component
        component = []
        queue = deque([start])
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            component.append(u)
            for v in friends[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        
        # Check if component is valid
        valid = True
        for i in range(len(component)):
            if not valid:
                break
            for j in range(i + 1, len(component)):
                if (min(component[i], component[j]), max(component[i], component[j])) in dislikes:
                    valid = False
                    break
        
        if valid:
            max_size = max(max_size, len(component))
    
    print(max_size)

solve()
