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

n, m = map(int, input().split())
edges = []
for i in range(m):
    w, t = map(int, input().split())
    edges.append((w, t, i))

# Count MST edges
mst_count = sum(1 for _, t, _ in edges if t == 1)
if mst_count != n - 1:
    print(-1)
else:
    # Sort by weight, MST edges first for same weight
    edges.sort(key=lambda x: (x[0], 1 - x[1]))
    
    parent = list(range(n))
    rank = [0] * n
    result = [None] * m
    valid = True
    
    for w, t, idx in edges:
        if t == 1:  # In MST
            # Find two vertices in different components
            u, v = -1, -1
            for i in range(n):
                if u == -1:
                    u = i
                elif find(parent, u) != find(parent, i):
                    v = i
                    break
            
            if v == -1:
                valid = False
                break
            
            union(parent, rank, u, v)
            result[idx] = (u + 1, v + 1)
        else:  # Not in MST
            # Find two vertices in the same component
            u, v = -1, -1
            for i in range(n):
                for j in range(i + 1, n):
                    if find(parent, i) == find(parent, j):
                        u, v = i, j
                        break
                if u != -1:
                    break
            
            if u == -1:
                valid = False
                break
            
            result[idx] = (u + 1, v + 1)
    
    if not valid:
        print(-1)
    else:
        for u, v in result:
            print(u, v)
