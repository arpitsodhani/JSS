import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    graph = [[] for _ in range(n + 1)]
    idx = 1
    
    for _ in range(n - 1):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
    
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    stack = [1]
    parent[1] = -1
    
    while stack:
        v = stack.pop()
        for to in graph[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            children[v].append(to)
            stack.append(to)
    
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    
    timer = 1
    left[1] = timer
    timer += 1
    
    stack = [1]
    while stack:
        v = stack.pop()
        
        for to in children[v]:
            left[to] = timer
            timer += 1
        
        right[v] = timer
        timer += 1
        
        for to in children[v]:
            stack.append(to)
    
    out = []
    for i in range(1, n + 1):
        out.append(f"{left[i]} {right[i]}")
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
