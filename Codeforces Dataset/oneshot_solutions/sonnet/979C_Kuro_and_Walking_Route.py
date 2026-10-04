import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, x, y = data[0], data[1], data[2]
    
    graph = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(n - 1):
        a, b = data[idx], data[idx + 1]
        idx += 2
        graph[a].append(b)
        graph[b].append(a)
    
    parent = [0] * (n + 1)
    order = []
    stack = [x]
    parent[x] = -1
    
    while stack:
        v = stack.pop()
        order.append(v)
        for to in graph[v]:
            if to != parent[v]:
                parent[to] = v
                stack.append(to)
    
    subtree = [1] * (n + 1)
    for v in reversed(order):
        for to in graph[v]:
            if parent[to] == v:
                subtree[v] += subtree[to]
    
    near_x = y
    while parent[near_x] != x:
        near_x = parent[near_x]
    
    x_side = n - subtree[near_x]
    y_side = subtree[y]
    
    print(n * (n - 1) - x_side * y_side)

if __name__ == "__main__":
    main()
