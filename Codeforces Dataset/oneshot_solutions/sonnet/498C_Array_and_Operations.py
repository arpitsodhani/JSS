import sys
from collections import defaultdict, deque

def prime_factorize(n):
    factors = defaultdict(int)
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] += 1
            n //= d
        d += 1
    if n > 1:
        factors[n] += 1
    return factors

def max_flow(edges, source, sink):
    graph = defaultdict(lambda: defaultdict(int))
    for u, v, cap in edges:
        graph[u][v] += cap
    
    def bfs():
        visited = {source}
        queue = deque([source])
        parent = {source: None}
        
        while queue:
            u = queue.popleft()
            if u == sink:
                return parent
            
            for v in graph[u]:
                if v not in visited and graph[u][v] > 0:
                    visited.add(v)
                    parent[v] = u
                    queue.append(v)
        
        return None
    
    total_flow = 0
    
    while True:
        parent = bfs()
        if parent is None:
            break
        
        path_flow = float('inf')
        v = sink
        while parent[v] is not None:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u
        
        v = sink
        while parent[v] is not None:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        
        total_flow += path_flow
    
    return total_flow

data = sys.stdin.read().split()
idx = 0

n = int(data[idx])
idx += 1
m = int(data[idx])
idx += 1

a = [0] + [int(data[idx + i]) for i in range(n)]
idx += n

pairs = []
for _ in range(m):
    i = int(data[idx])
    j = int(data[idx + 1])
    pairs.append((i, j))
    idx += 2

factors = [None] + [prime_factorize(a[i]) for i in range(1, n + 1)]

all_primes = set()
for i in range(1, n + 1):
    all_primes.update(factors[i].keys())

total_ops = 0

for prime in all_primes:
    edges = []
    source = 'S'
    sink = 'T'
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            cap = factors[i].get(prime, 0)
            if cap > 0:
                edges.append((source, ('odd', i), cap))
    
    for i, j in pairs:
        i_odd = (i % 2 == 1)
        j_odd = (j % 2 == 1)
        
        if i_odd and not j_odd:
            if factors[i].get(prime, 0) > 0 and factors[j].get(prime, 0) > 0:
                edges.append((('odd', i), ('even', j), 10**9))
        elif not i_odd and j_odd:
            if factors[i].get(prime, 0) > 0 and factors[j].get(prime, 0) > 0:
                edges.append((('odd', j), ('even', i), 10**9))
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            cap = factors[i].get(prime, 0)
            if cap > 0:
                edges.append((('even', i), sink, cap))
    
    flow = max_flow(edges, source, sink)
    total_ops += flow

print(total_ops)
