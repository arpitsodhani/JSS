import sys
from collections import deque

def solve():
    lines = sys.stdin.read().strip().split('\n')
    n, m = map(int, lines[0].split())
    
    edges = []
    for i in range(1, m + 1):
        parts = list(map(int, lines[i].split()))
        if len(parts) >= 4:
            u, v, w, b = parts[0], parts[1], parts[2], parts[3]
            edges.append((u, v, w, b))
        elif len(parts) == 3:
            edges.append((parts[0], parts[1], parts[2], None))
        else:
            edges.append((parts[0], parts[1], None, None))
    
    # Check if we have complete information
    if any(e[2] is None or e[3] is None for e in edges):
        print("UNKNOWN")
        return
    
    # Check flow conservation
    balance = [0.0] * (n + 1)
    for u, v, w, b in edges:
        balance[u] -= b
        balance[v] += b
    
    k = -balance[1]
    if k <= 0:
        print("BAD 1")
        return
        
    for i in range(1, n + 1):
        expected = -k if i == 1 else (k if i == n else 0)
        if abs(balance[i] - expected) > 1e-9:
            print("BAD 1")
            return
    
    # Compute node potentials
    potential = [None] * (n + 1)
    potential[1] = 0.0
    
    # Iteratively propagate potentials
    for _ in range(n):
        for u, v, w, b in edges:
            if abs(b) > 1e-9:  # Positive flow
                if potential[u] is not None and potential[v] is None:
                    potential[v] = potential[u] + 2 * w * b
                elif potential[v] is not None and potential[u] is None:
                    potential[u] = potential[v] - 2 * w * b
            else:  # Zero flow
                if potential[u] is not None and potential[v] is None:
                    potential[v] = potential[u]
                elif potential[v] is not None and potential[u] is None:
                    potential[u] = potential[v]
    
    # Check if all potentials computed
    if any(p is None for p in potential[1:n+1]):
        print("UNKNOWN")
        return
    
    # Verify optimality conditions
    for idx, (u, v, w, b) in enumerate(edges):
        if abs(b) > 1e-9:  # Positive flow
            if abs(potential[v] - potential[u] - 2 * w * b) > 1e-6:
                print("BAD", idx + 1)
                return
        else:  # Zero flow
            if abs(potential[v] - potential[u]) > 1e-6:
                print("BAD", idx + 1)
                return
    
    # Flow is optimal, compute cost
    cost = sum(w * b * b for u, v, w, b in edges)
    print(int(round(cost)))

solve()
