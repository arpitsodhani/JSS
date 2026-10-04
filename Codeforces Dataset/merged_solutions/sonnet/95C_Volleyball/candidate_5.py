# CLAUSE: setup_environment
import sys
from heapq import heappop, heappush

INF = 10 ** 30

def reachable_by_taxi(origin, roads, limit):
    n = len(roads)
    dist = [INF] * n
    dist[origin] = 0
    heap = [(0, origin)]
    reached = []
    while heap:
        d, v = heappop(heap)
        if d != dist[v]:
            continue
        if d > limit:
            continue
        reached.append(v)
        for to, w in roads[v]:
            nd = d + w
            if nd < dist[to] and nd <= limit:
                dist[to] = nd
                heappush(heap, (nd, to))
    return reached

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    x = data[idx] - 1
    y = data[idx + 1] - 1
    idx += 2

    roads = [[] for _ in range(n)]
    for _ in range(m):
        a = data[idx] - 1
        b = data[idx + 1] - 1
        w = data[idx + 2]
        idx += 3
        roads[a].append((b, w))
        roads[b].append((a, w))

    limits = [0] * n
    costs = [0] * n
    for city in range(n):
        limits[city] = data[idx]
        costs[city] = data[idx + 1]
        idx += 2

    fares = [INF] * n
    fares[x] = 0
    expanded = [None] * n
    heap = [(0, x)]

    while heap:
        total, city = heappop(heap)
        if total != fares[city]:
            continue
        if city == y:
            break
        if expanded[city] is None:
            expanded[city] = reachable_by_taxi(city, roads, limits[city])
        ntotal = total + costs[city]
        for nxt in expanded[city]:
            if ntotal < fares[nxt]:
                fares[nxt] = ntotal
                heappush(heap, (ntotal, nxt))

    print(fares[y])

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
