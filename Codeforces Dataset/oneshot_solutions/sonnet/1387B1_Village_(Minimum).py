import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    n = int(data[0])
    graph = [[] for _ in range(n + 1)]
    idx = 1
    
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
    
    parent = [0] * (n + 1)
    order = [1]
    parent[1] = -1
    
    for v in order:
        for to in graph[v]:
            if to != parent[v]:
                parent[to] = v
                order.append(to)
    
    matched = [False] * (n + 1)
    chosen = set()
    
    for v in reversed(order[1:]):
        p = parent[v]
        if not matched[v] and not matched[p]:
            matched[v] = True
            matched[p] = True
            chosen.add((min(v, p), max(v, p)))
    
    for v in range(1, n + 1):
        if not matched[v]:
            to = parent[v] if parent[v] != -1 else graph[v][0]
            chosen.add((min(v, to), max(v, to)))
    
    forest = [[] for _ in range(n + 1)]
    for u, v in chosen:
        forest[u].append(v)
        forest[v].append(u)
    
    answer = [0] * (n + 1)
    seen = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if seen[start]:
            continue
        
        stack = [start]
        seen[start] = True
        comp = []
        
        while stack:
            v = stack.pop()
            comp.append(v)
            for to in forest[v]:
                if not seen[to]:
                    seen[to] = True
                    stack.append(to)
        
        k = len(comp)
        for i in range(k):
            answer[comp[i]] = comp[(i + 1) % k]
    
    print(2 * len(chosen))
    print(' '.join(map(str, answer[1:])))

if __name__ == "__main__":
    main()
