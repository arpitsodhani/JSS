import sys
from collections import defaultdict
sys.setrecursionlimit(500000)

def solve():
    data = sys.stdin.buffer.read().decode('utf-8').split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    if m == 0:
        return
    
    if m % 2 == 1:
        print("No solution")
        return
    
    edges = []
    graph = defaultdict(list)
    for i in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u, v))
        graph[u].append((v, i))
        graph[v].append((u, i))
    
    used = [False] * m
    pairs = []
    
    def dfs(v, entering_edge_id):
        unpaired = entering_edge_id
        
        for u, eid in graph[v]:
            if used[eid]:
                continue
            
            used[eid] = True
            
            returned = dfs(u, eid)
            
            if returned is not None:
                if unpaired is None:
                    unpaired = returned
                else:
                    pairs.append((unpaired, returned))
                    unpaired = None
        
        return unpaired
    
    # Handle all connected components
    for start_vertex in range(1, n + 1):
        if any(not used[eid] for _, eid in graph[start_vertex]):
            result = dfs(start_vertex, None)
            if result is not None:
                print("No solution")
                return
    
    # Check if all edges are used
    if len(pairs) != m // 2:
        print("No solution")
        return
    
    # Output the pairs
    for e1, e2 in pairs:
        u1, v1 = edges[e1]
        u2, v2 = edges[e2]
        # Find common vertex and output the path
        if u1 == u2:
            print(v1, u1, v2)
        elif u1 == v2:
            print(v1, u1, u2)
        elif v1 == u2:
            print(u1, v1, v2)
        else:  # v1 == v2
            print(u1, v1, u2)

solve()
