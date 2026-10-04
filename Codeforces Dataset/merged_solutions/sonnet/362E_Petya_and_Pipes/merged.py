import sys
FAR = 10 ** 18
WIDE = 10 ** 9

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    matrix = []
    pos = 2
    for _ in range(n):
        matrix.append(data[pos:pos + n])
        pos += n
    return n, k, matrix

# Clause build_graph [Confidence: 1.00]
def build_graph(n, matrix):
    graph = [[] for _ in range(n)]
    to = []
    cap = []
    cost = []
    for i in range(n):
        row = matrix[i]
        for j in range(n):
            width = row[j]
            if width:
                graph[i].append(len(to))
                to.append(j)
                cap.append(width)
                cost.append(0)
                graph[j].append(len(to))
                to.append(i)
                cap.append(0)
                cost.append(0)
                graph[i].append(len(to))
                to.append(j)
                cap.append(WIDE)
                cost.append(1)
                graph[j].append(len(to))
                to.append(i)
                cap.append(0)
                cost.append(-1)
    return graph, to, cap, cost

# Clause free_max_flow [Confidence: 1.00]
def free_max_flow(n, graph, to, cap, cost):
    sink = n - 1
    total = 0
    while True:
        level = [-1] * n
        level[0] = 0
        queue = [0]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for e in graph[u]:
                v = to[e]
                if cap[e] > 0 and cost[e] == 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        if level[sink] < 0:
            return total
        arc = [0] * n
        while True:
            stack = [0]
            path = []
            while stack and stack[-1] != sink:
                u = stack[-1]
                moved = False
                while arc[u] < len(graph[u]):
                    e = graph[u][arc[u]]
                    v = to[e]
                    if cap[e] > 0 and cost[e] == 0 and level[v] == level[u] + 1:
                        stack.append(v)
                        path.append(e)
                        moved = True
                        break
                    arc[u] += 1
                if not moved:
                    level[u] = -1
                    stack.pop()
                    if path:
                        path.pop()
            if not stack:
                break
            push = min(cap[e] for e in path)
            for e in path:
                cap[e] -= push
                cap[e ^ 1] += push
            total += push

# Clause paid_augment [Confidence: 1.00]
def paid_augment(n, k, graph, to, cap, cost):
    sink = n - 1
    budget = k
    extra = 0
    while budget > 0:
        dist = [FAR] * n
        dist[0] = 0
        prev = [-1] * n
        queued = [False] * n
        queue = [0]
        queued[0] = True
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            queued[u] = False
            base = dist[u]
            for e in graph[u]:
                if cap[e] > 0:
                    v = to[e]
                    step = base + cost[e]
                    if step < dist[v]:
                        dist[v] = step
                        prev[v] = e
                        if not queued[v]:
                            queued[v] = True
                            queue.append(v)
        if dist[sink] >= FAR:
            break
        price = dist[sink]
        room = FAR
        node = sink
        while node:
            e = prev[node]
            if cap[e] < room:
                room = cap[e]
            node = to[e ^ 1]
        push = room if price <= 0 else min(room, budget // price)
        if push <= 0:
            break
        node = sink
        while node:
            e = prev[node]
            cap[e] -= push
            cap[e ^ 1] += push
            node = to[e ^ 1]
        budget -= push * price
        extra += push
    return extra

# Clause solve [Confidence: 1.00]
def solve(n, k, matrix):
    graph, to, cap, cost = build_graph(n, matrix)
    base = free_max_flow(n, graph, to, cap, cost)
    return base + paid_augment(n, k, graph, to, cap, cost)

# Clause main [Confidence: 1.00]
def main():
    n, k, matrix = read_input()
    sys.stdout.write(str(solve(n, k, matrix)) + "\n")


if __name__ == "__main__":
    main()

