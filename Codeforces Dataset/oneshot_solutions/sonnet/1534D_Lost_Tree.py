def solve():
    n = int(input())
    
    # Query from node 1
    print("? 1", flush=True)
    d1 = list(map(int, input().split()))
    
    # Partition nodes by distance parity from node 1
    even_nodes = [i + 1 for i in range(n) if d1[i] % 2 == 0 and i + 1 != 1]
    odd_nodes = [i + 1 for i in range(n) if d1[i] % 2 == 1]
    
    # Choose the smaller set to query from
    if len(even_nodes) <= len(odd_nodes):
        query_nodes = even_nodes
    else:
        query_nodes = odd_nodes
    
    # Collect all edges
    edges = []
    
    # Add edges from node 1 to its neighbors
    for i in range(n):
        if d1[i] == 1:
            edges.append((1, i + 1))
    
    # Query from other nodes in the chosen set
    for node in query_nodes:
        print(f"? {node}", flush=True)
        d = list(map(int, input().split()))
        for i in range(n):
            u = i + 1
            if d[i] == 1 and u != node and u != 1:
                # u is adjacent to node
                if d1[i] < d1[node - 1]:
                    # u is closer to node 1
                    edges.append((u, node))
                else:
                    # node is closer to node 1
                    edges.append((node, u))
    
    # Output the result
    print("!")
    for u, v in edges:
        print(u, v)

solve()
