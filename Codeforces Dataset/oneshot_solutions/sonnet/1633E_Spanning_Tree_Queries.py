import sys

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

def get_spanning_tree(n, edges, x):
    indexed_edges = [(abs(e[2] - x), e[2], i, e) for i, e in enumerate(edges)]
    indexed_edges.sort()
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    tree_edges = []
    for _, _, _, (u, v, w) in indexed_edges:
        if union(parent, rank, u, v):
            tree_edges.append(w)
            if len(tree_edges) == n - 1:
                break
    return tuple(sorted(tree_edges))

def compute_cost(tree_weights, x):
    return sum(abs(w - x) for w in tree_weights)

def main():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        w = int(data[idx + 2])
        edges.append((u, v, w))
        idx += 3
    
    p = int(data[idx])
    k = int(data[idx + 1])
    a = int(data[idx + 2])
    b = int(data[idx + 3])
    c = int(data[idx + 4])
    idx += 5
    
    queries = []
    for _ in range(p):
        queries.append(int(data[idx]))
        idx += 1
    
    for j in range(p, k):
        queries.append((queries[-1] * a + b) % c)
    
    candidates_set = set()
    edge_weights = sorted(set(e[2] for e in edges))
    
    sample_x_values = set(edge_weights)
    for i in range(len(edge_weights)):
        for j in range(i + 1, len(edge_weights)):
            mid = (edge_weights[i] + edge_weights[j]) // 2
            sample_x_values.add(mid)
            sample_x_values.add(mid + 1)
    
    sample_x_values.add(0)
    if edge_weights:
        sample_x_values.add(edge_weights[-1] + 1000000)
    
    for x in sample_x_values:
        st = get_spanning_tree(n, edges, x)
        candidates_set.add(st)
    
    candidates = list(candidates_set)
    
    result = 0
    for x in queries:
        best_cost = min(compute_cost(candidate, x) for candidate in candidates)
        result ^= best_cost
    
    print(result)

if __name__ == "__main__":
    main()
