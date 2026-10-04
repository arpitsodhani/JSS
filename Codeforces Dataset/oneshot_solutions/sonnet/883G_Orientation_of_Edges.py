import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    s = data[idx + 2]
    idx += 3
    
    directed = [[] for _ in range(n + 1)]
    mixed = [[] for _ in range(n + 1)]
    undirected_edges = []
    edge_id = 0
    
    for _ in range(m):
        typ = data[idx]
        u = data[idx + 1]
        v = data[idx + 2]
        idx += 3
        
        if typ == 1:
            directed[u].append(v)
            mixed[u].append((v, -1, 0))
        else:
            undirected_edges.append((u, v))
            mixed[u].append((v, edge_id, 1))
            mixed[v].append((u, edge_id, -1))
            edge_id += 1
    
    k = len(undirected_edges)
    
    # Minimum: only vertices reachable through already directed edges are unavoidable.
    reachable_min = [False] * (n + 1)
    q = deque([s])
    reachable_min[s] = True
    
    while q:
        v = q.popleft()
        for to in directed[v]:
            if not reachable_min[to]:
                reachable_min[to] = True
                q.append(to)
    
    min_answer = ['+'] * k
    for i, (u, v) in enumerate(undirected_edges):
        if reachable_min[u] and not reachable_min[v]:
            min_answer[i] = '-'
        else:
            min_answer[i] = '+'
    
    # Maximum: traverse the graph where undirected edges can be used both ways,
    # and orient each used undirected edge in the traversal direction.
    reachable_max = [False] * (n + 1)
    max_answer = ['+'] * k
    q = deque([s])
    reachable_max[s] = True
    
    while q:
        v = q.popleft()
        for to, eid, direction in mixed[v]:
            if not reachable_max[to]:
                reachable_max[to] = True
                q.append(to)
                
                if eid != -1:
                    max_answer[eid] = '+' if direction == 1 else '-'
    
    print(sum(reachable_max))
    print(''.join(max_answer))
    print(sum(reachable_min))
    print(''.join(min_answer))

if __name__ == "__main__":
    main()
