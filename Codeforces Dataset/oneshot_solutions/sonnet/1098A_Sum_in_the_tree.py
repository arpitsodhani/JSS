import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().decode().strip().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    
    if n == 1:
        s1 = int(data[idx])
        print(s1)
        return
    
    # Read parents
    parents = [0, 0]
    for _ in range(n - 1):
        parents.append(int(data[idx]))
        idx += 1
    
    # Read s values
    s = [0]
    for _ in range(n):
        s.append(int(data[idx]))
        idx += 1
    
    # Build children lists
    children = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        children[parents[i]].append(i)
    
    # Compute depths using BFS
    depth = [0] * (n + 1)
    depth[1] = 1
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for c in children[v]:
            depth[c] = depth[v] + 1
            queue.append(c)
    
    # Compute s values for even-depth vertices
    queue = deque([1])
    while queue:
        v = queue.popleft()
        
        if depth[v] % 2 == 0:  # Even depth
            parent_s = s[parents[v]]
            if children[v]:
                min_child_s = min(s[c] for c in children[v])
                if min_child_s < parent_s:
                    print(-1)
                    return
                s[v] = min_child_s
            else:
                s[v] = parent_s
        
        for c in children[v]:
            queue.append(c)
    
    # Compute sum of a values
    total = s[1]
    for i in range(2, n + 1):
        a_i = s[i] - s[parents[i]]
        if a_i < 0:
            print(-1)
            return
        total += a_i
    
    print(total)

solve()
