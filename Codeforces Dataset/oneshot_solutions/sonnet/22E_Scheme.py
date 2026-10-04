import sys

sys.setrecursionlimit(300000)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    f = [0] + data[1:n + 1]
    
    graph = [[] for _ in range(n + 1)]
    rev = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i].append(f[i])
        rev[f[i]].append(i)
    
    visited = [False] * (n + 1)
    order = []
    
    def dfs1(v):
        visited[v] = True
        for to in graph[v]:
            if not visited[to]:
                dfs1(to)
        order.append(v)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i)
    
    comp = [0] * (n + 1)
    reps = []
    
    def dfs2(v, c):
        comp[v] = c
        for to in rev[v]:
            if comp[to] == 0:
                dfs2(to, c)
    
    comp_count = 0
    for v in reversed(order):
        if comp[v] == 0:
            comp_count += 1
            reps.append(v)
            dfs2(v, comp_count)
    
    if comp_count == 1:
        print(0)
        return
    
    indeg = [0] * (comp_count + 1)
    outdeg = [0] * (comp_count + 1)
    
    for v in range(1, n + 1):
        a = comp[v]
        b = comp[f[v]]
        if a != b:
            outdeg[a] += 1
            indeg[b] += 1
    
    sources = []
    sinks = []
    for c in range(1, comp_count + 1):
        if indeg[c] == 0:
            sources.append(c)
        if outdeg[c] == 0:
            sinks.append(c)
    
    k = max(len(sources), len(sinks))
    result = []
    
    for i in range(k):
        sink = sinks[i % len(sinks)]
        source = sources[(i + 1) % len(sources)]
        result.append((reps[sink - 1], reps[source - 1]))
    
    print(k)
    for x, y in result:
        print(x, y)

if __name__ == "__main__":
    main()
