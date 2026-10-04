# CLAUSE: setup_environment
import sys
import heapq

INF = 10 ** 30

def shortest_from(start, graph, n):
    dist = [INF] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, v = heapq.heappop(heap)
        if d != dist[v]:
            continue
        for to, w in graph[v]:
            nd = d + w
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(heap, (nd, to))
    return dist

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    n, m = data[p], data[p + 1]
    p += 2
    x, y = data[p] - 1, data[p + 1] - 1
    p += 2

    roads = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = data[p] - 1, data[p + 1] - 1, data[p + 2]
        p += 3
        roads[a].append((b, w))
        roads[b].append((a, w))

    limit = [0] * n
    price = [0] * n
    for i in range(n):
        limit[i], price[i] = data[p], data[p + 1]
        p += 2

    road_dist = [shortest_from(i, roads, n) for i in range(n)]

    fare = [INF] * n
    fare[x] = 0
    heap = [(0, x)]
    while heap:
        cur, v = heapq.heappop(heap)
        if cur != fare[v]:
            continue
        if v == y:
            break
        add = price[v]
        reach = limit[v]
        row = road_dist[v]
        for to, d in enumerate(row):
            nd = cur + add
            if d <= reach and nd < fare[to]:
                fare[to] = nd
                heapq.heappush(heap, (nd, to))

    print(fare[y])

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
