from collections import defaultdict, deque

def solve():
    n, k = map(int, input().split())
    if n == 0:
        print(0)
        return
    
    mines = []
    for _ in range(n):
        x, y, t = map(int, input().split())
        mines.append((x, y, t))
    
    # Group mines by x and y coordinates
    by_x = defaultdict(list)
    by_y = defaultdict(list)
    
    for i, (x, y, t) in enumerate(mines):
        by_x[x].append(i)
        by_y[y].append(i)
    
    # Build adjacency list
    adj = [set() for _ in range(n)]
    
    # Connect mines on the same x-coordinate within distance k
    for indices in by_x.values():
        indices_sorted = sorted(indices, key=lambda i: mines[i][1])
        for j in range(len(indices_sorted)):
            for l in range(j + 1, len(indices_sorted)):
                i1, i2 = indices_sorted[j], indices_sorted[l]
                if abs(mines[i1][1] - mines[i2][1]) <= k:
                    adj[i1].add(i2)
                    adj[i2].add(i1)
                else:
                    break
    
    # Connect mines on the same y-coordinate within distance k
    for indices in by_y.values():
        indices_sorted = sorted(indices, key=lambda i: mines[i][0])
        for j in range(len(indices_sorted)):
            for l in range(j + 1, len(indices_sorted)):
                i1, i2 = indices_sorted[j], indices_sorted[l]
                if abs(mines[i1][0] - mines[i2][0]) <= k:
                    adj[i1].add(i2)
                    adj[i2].add(i1)
                else:
                    break
    
    # Find connected components using BFS
    visited = [False] * n
    components = []
    
    for i in range(n):
        if not visited[i]:
            component = []
            queue = deque([i])
            visited[i] = True
            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            min_time = min(mines[j][2] for j in component)
            components.append(min_time)
    
    # Sort components by minimum lifetime
    components.sort()
    
    # Binary search for the answer
    def check(T):
        count = sum(1 for min_time in components if min_time > T)
        return count <= T + 1
    
    left, right = 0, max(t for _, _, t in mines)
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    
    print(left)

t = int(input())
for _ in range(t):
    solve()
