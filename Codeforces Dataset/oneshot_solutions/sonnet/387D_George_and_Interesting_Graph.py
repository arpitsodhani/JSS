def solve():
    n, m = map(int, input().split())
    
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u-1, v-1))
    
    if n == 1:
        self_loop_exists = any(u == 0 and v == 0 for u, v in edges)
        changes = m - (1 if self_loop_exists else 0) + (0 if self_loop_exists else 1)
        print(changes)
        return
    
    edge_set = set(edges)
    min_changes = float('inf')
    
    for center in range(n):
        changes = 0
        
        # Required edges involving center
        required_center = set()
        required_center.add((center, center))
        for u in range(n):
            if u != center:
                required_center.add((u, center))
                required_center.add((center, u))
        
        # Count changes for center edges
        for edge in required_center:
            if edge not in edge_set:
                changes += 1
        
        for edge in edges:
            if (edge[0] == center or edge[1] == center) and edge not in required_center:
                changes += 1
        
        # Count degrees for non-center vertices
        outdeg = [0] * n
        indeg = [0] * n
        
        for u, v in edges:
            if u != center and v != center:
                outdeg[u] += 1
                indeg[v] += 1
        
        # Calculate cost for non-center vertices
        cost_noncenter = sum(abs(outdeg[u] - 1) for u in range(n) if u != center)
        cost_noncenter += sum(abs(indeg[u] - 1) for u in range(n) if u != center)
        cost_noncenter //= 2
        
        changes += cost_noncenter
        
        min_changes = min(min_changes, changes)
    
    print(min_changes)

solve()
