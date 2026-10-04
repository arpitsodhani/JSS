from collections import deque

def check_order(n, battles):
    if not battles:
        return 0
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for u, v in battles:
        adj[u].append(v)
    
    # Compute transitive closure using BFS
    reach = [[False] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        queue = deque([i])
        visited[i] = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                reach[i][v] = True
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
    
    # Check for cycles (contradiction)
    for i in range(1, n + 1):
        if reach[i][i]:
            return -1
    
    # Check if all pairs are comparable
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if not reach[i][j] and not reach[j][i]:
                return 0
    
    return 1

n, m = map(int, input().split())
battles = []
for _ in range(m):
    a, b = map(int, input().split())
    battles.append((a, b))

for k in range(1, m + 1):
    result = check_order(n, battles[:k])
    if result == -1:
        print(-1)
        break
    elif result == 1:
        print(k)
        break
else:
    print(-1)
