import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    
    n = int(data[idx])
    idx += 1
    
    colors = [0] + [int(data[idx + i]) for i in range(n)]
    idx += n
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
    
    total_red = colors.count(1)
    total_blue = colors.count(2)
    
    parent = [0] * (n + 1)
    order = [1]
    parent[1] = -1
    
    for v in order:
        for to in graph[v]:
            if to != parent[v]:
                parent[to] = v
                order.append(to)
    
    red = [0] * (n + 1)
    blue = [0] * (n + 1)
    answer = 0
    
    for v in reversed(order):
        if colors[v] == 1:
            red[v] += 1
        elif colors[v] == 2:
            blue[v] += 1
        
        for to in graph[v]:
            if parent[to] == v:
                red[v] += red[to]
                blue[v] += blue[to]
        
        if v != 1:
            if red[v] == total_red and blue[v] == 0:
                answer += 1
            elif blue[v] == total_blue and red[v] == 0:
                answer += 1
    
    print(answer)

if __name__ == "__main__":
    main()
