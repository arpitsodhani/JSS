import sys
from itertools import permutations

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    
    n = int(data[idx])
    idx += 1
    
    cost = [[0] * n for _ in range(3)]
    for color in range(3):
        for i in range(n):
            cost[color][i] = int(data[idx])
            idx += 1
    
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
    
    if n == 1:
        best_color = min(range(3), key=lambda c: cost[c][0])
        print(cost[best_color][0])
        print(best_color + 1)
        return
    
    if n == 2:
        answer = []
        total = 0
        for i in range(2):
            best_color = min(range(3), key=lambda c: cost[c][i])
            answer.append(best_color + 1)
            total += cost[best_color][i]
        print(total)
        print(*answer)
        return
    
    for i in range(n):
        if len(graph[i]) > 2:
            print(-1)
            return
    
    start = 0
    for i in range(n):
        if len(graph[i]) == 1:
            start = i
            break
    
    order = []
    parent = -1
    current = start
    
    while current != -1:
        order.append(current)
        nxt = -1
        for to in graph[current]:
            if to != parent:
                nxt = to
                break
        parent, current = current, nxt
    
    best_cost = 10 ** 30
    best_colors = None
    
    for perm in permutations(range(3)):
        total = 0
        colors = [0] * n
        
        for pos, vertex in enumerate(order):
            color = perm[pos % 3]
            total += cost[color][vertex]
            colors[vertex] = color + 1
        
        if total < best_cost:
            best_cost = total
            best_colors = colors
    
    print(best_cost)
    print(*best_colors)

if __name__ == "__main__":
    main()
