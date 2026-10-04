from math import gcd

def solve():
    n, m = map(int, input().split())
    
    # Minimum edges for connected graph
    if m < n - 1:
        print("Impossible")
        return
    
    # Generate all coprime pairs
    all_edges = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if gcd(i, j) == 1:
                all_edges.append((i, j))
    
    # Check if we have enough coprime pairs
    if len(all_edges) < m:
        print("Impossible")
        return
    
    # Build a connected graph
    # Use star topology centered at vertex 1
    selected = []
    selected_set = set()
    
    # First, add edges from vertex 1 to all others (these are all coprime)
    for i in range(2, n + 1):
        selected.append((1, i))
        selected_set.add((1, i))
    
    # Then add remaining edges from the list
    for edge in all_edges:
        if len(selected) >= m:
            break
        if edge not in selected_set:
            selected.append(edge)
            selected_set.add(edge)
    
    print("Possible")
    for u, v in selected:
        print(u, v)

solve()
