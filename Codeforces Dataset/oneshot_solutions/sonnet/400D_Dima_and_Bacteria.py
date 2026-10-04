import sys
from collections import defaultdict
import heapq

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx])
    k = int(input_data[idx + 1])
    m = int(input_data[idx + 2])
    idx += 3
    
    c = []
    for i in range(k):
        c.append(int(input_data[idx]))
        idx += 1
    
    # Determine which bacteria belong to which type
    bacteria_type = [0] * (n + 1)  # 1-indexed
    bac_id = 1
    for type_id in range(k):
        for _ in range(c[type_id]):
            bacteria_type[bac_id] = type_id
            bac_id += 1
    
    # Build adjacency list
    edges = []
    graph = defaultdict(list)
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        x = int(input_data[idx + 2])
        idx += 3
        edges.append((u, v, x))
        graph[u].append((v, x))
        graph[v].append((u, x))
    
    # Step 1: Check if type-distribution is correct using DSU with 0-cost edges
    parent = list(range(n + 1))
    
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        # Path compression
        while parent[x] != root:
            next_x = parent[x]
            parent[x] = root
            x = next_x
        return root
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # Union only 0-cost edges
    for u, v, x in edges:
        if x == 0:
            union(u, v)
    
    # Check if all bacteria of the same type are in the same component
    for type_id in range(k):
        bacteria_of_type = [i for i in range(1, n + 1) if bacteria_type[i] == type_id]
        if len(bacteria_of_type) > 1:
            root = find(bacteria_of_type[0])
            for b in bacteria_of_type[1:]:
                if find(b) != root:
                    print("No")
                    return
    
    print("Yes")
    
    # Step 2: Compute shortest paths
    def dijkstra(start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        
        return dist
    
    # Pick one representative for each type
    type_rep = [0] * k
    for i in range(1, n + 1):
        t = bacteria_type[i]
        if type_rep[t] == 0:
            type_rep[t] = i
    
    # Distance matrix
    d = [[float('inf')] * k for _ in range(k)]
    
    for i in range(k):
        rep_i = type_rep[i]
        dist = dijkstra(rep_i)
        
        for j in range(k):
            rep_j = type_rep[j]
            d[i][j] = dist[rep_j]
    
    # Print the matrix
    for i in range(k):
        row = []
        for j in range(k):
            if d[i][j] == float('inf'):
                row.append(-1)
            else:
                row.append(d[i][j])
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
