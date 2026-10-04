import sys
sys.setrecursionlimit(300000)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def main():
    input_data = sys.stdin.buffer.read().decode('utf-8').strip().split('\n')
    idx = 0
    
    n, m = map(int, input_data[idx].split())
    idx += 1
    
    a = list(map(int, input_data[idx].split()))
    idx += 1
    
    # Find vertex with minimum value
    min_val = min(a)
    min_idx = a.index(min_val)
    
    # Collect all edges
    edges = []
    
    # Add edges from min vertex to all others
    for i in range(n):
        if i != min_idx:
            edges.append((a[min_idx] + a[i], min_idx, i))
    
    # Add special offers
    for _ in range(m):
        x, y, w = map(int, input_data[idx].split())
        x -= 1  # 0-indexed
        y -= 1
        edges.append((w, x, y))
        idx += 1
    
    # Sort edges by cost
    edges.sort()
    
    # Kruskal's algorithm
    parent = list(range(n))
    rank = [0] * n
    total_cost = 0
    edges_added = 0
    
    for cost, x, y in edges:
        if union(parent, rank, x, y):
            total_cost += cost
            edges_added += 1
            if edges_added == n - 1:
                break
    
    print(total_cost)

if __name__ == "__main__":
    main()
