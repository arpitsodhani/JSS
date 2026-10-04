import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        graph[a].append(b)
        graph[b].append(a)
    
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    
    timer = 0
    stack = [(1, 0, 0)]
    parent[1] = 1
    
    while stack:
        v, p, state = stack.pop()
        if state == 0:
            timer += 1
            tin[v] = timer
            stack.append((v, p, 1))
            
            for to in graph[v]:
                if to == p:
                    continue
                parent[to] = v
                depth[to] = depth[v] + 1
                stack.append((to, v, 0))
        else:
            tout[v] = timer
    
    def is_ancestor(a, b):
        return tin[a] <= tin[b] and tout[b] <= tout[a]
    
    answers = []
    
    for _ in range(m):
        k = data[idx]
        idx += 1
        
        nodes = []
        deepest = 1
        
        for _ in range(k):
            v = data[idx]
            idx += 1
            
            if v != 1:
                v = parent[v]
            
            nodes.append(v)
            if depth[v] > depth[deepest]:
                deepest = v
        
        ok = True
        for v in nodes:
            if not is_ancestor(v, deepest):
                ok = False
                break
        
        answers.append("YES" if ok else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
