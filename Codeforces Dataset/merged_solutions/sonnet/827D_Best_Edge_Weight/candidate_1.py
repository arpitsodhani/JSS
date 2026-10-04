# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    edges = []
    for i in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        w = int(data[idx + 2])
        idx += 3
        edges.append((w, u, v, i))
    
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True
    
    tree = [[] for _ in range(n + 1)]
    in_mst = [False] * m
    
    for w, u, v, i in sorted(edges):
        if union(u, v):
            in_mst[i] = True
            tree[u].append((v, w, i))
            tree[v].append((u, w, i))
    
    log = (n + 1).bit_length()
    up = [[0] * (n + 1) for _ in range(log)]
    mx = [[0] * (n + 1) for _ in range(log)]
    depth = [0] * (n + 1)
    edge_to_parent = [-1] * (n + 1)
    
    stack = [(1, 0)]
    order = []
    while stack:
        v, p = stack.pop()
        order.append(v)
        up[0][v] = p
        for to, w, eid in tree[v]:
            if to == p:
                continue
            depth[to] = depth[v] + 1
            mx[0][to] = w
            edge_to_parent[to] = eid
            stack.append((to, v))
    
    for j in range(1, log):
        prev_up = up[j - 1]
        cur_up = up[j]
        prev_mx = mx[j - 1]
        cur_mx = mx[j]
        for v in range(1, n + 1):
            mid = prev_up[v]
            cur_up[v] = prev_up[mid]
            cur_mx[v] = max(prev_mx[v], prev_mx[mid])
    
    def max_on_path(a, b):
        result = 0
        if depth[a] < depth[b]:
            a, b = b, a
        
        diff = depth[a] - depth[b]
        bit = 0
        while diff:
            if diff & 1:
                result = max(result, mx[bit][a])
                a = up[bit][a]
            diff >>= 1
            bit += 1
        
        if a == b:
            return result
        
        for j in range(log - 1, -1, -1):
            if up[j][a] != up[j][b]:
                result = max(result, mx[j][a], mx[j][b])
                a = up[j][a]
                b = up[j][b]
        
        return max(result, mx[0][a], mx[0][b])
    
    answer = [-1] * m
    best = [10 ** 30] * (n + 1)
    
    for w, u, v, i in edges:
        if not in_mst[i]:
            answer[i] = max_on_path(u, v) - 1
            best[u] = min(best[u], w)
            best[v] = min(best[v], w)
    
    for j in range(log - 1, -1, -1):
        for w, u, v, i in edges:
            if in_mst[i]:
                continue
            a, b = u, v
            if depth[a] < depth[b]:
                a, b = b, a
            if depth[a] - (1 << j) >= depth[b]:
                best[a] = min(best[a], w)
                a = up[j][a]
                u = a
                v = b
    
    for w, u, v, i in edges:
        if in_mst[i]:
            continue
        a, b = u, v
        while depth[a] > depth[b]:
            best[a] = min(best[a], w)
            a = up[0][a]
        while depth[b] > depth[a]:
            best[b] = min(best[b], w)
            b = up[0][b]
        while a != b:
            best[a] = min(best[a], w)
            best[b] = min(best[b], w)
            a = up[0][a]
            b = up[0][b]
    
    for v in range(2, n + 1):
        eid = edge_to_parent[v]
        if best[v] < 10 ** 30:
            answer[eid] = best[v] - 1
    
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
