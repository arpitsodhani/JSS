# CLAUSE: setup_environment
import sys
from heapq import heappush, heappop

INF = 10 ** 30

def bounded_dijkstra(source, roads, cap, n):
    dist = [INF] * n
    dist[source] = 0
    pq = [(0, source)]
    reachable = []
    while pq:
        d, v = heappop(pq)
        if d != dist[v]:
            continue
        if d > cap:
            continue
        reachable.append(v)
        for u, w in roads[v]:
            nd = d + w
            if nd <= cap and nd < dist[u]:
                dist[u] = nd
                heappush(pq, (nd, u))
    return reachable

# CLAUSE: solve_logic
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(nums)
    n = next(it)
    m = next(it)
    x = next(it) - 1
    y = next(it) - 1

    roads = [[] for _ in range(n)]
    for _ in range(m):
        a = next(it) - 1
        b = next(it) - 1
        w = next(it)
        roads[a].append((b, w))
        roads[b].append((a, w))

    reach_limit = []
    ride_cost = []
    for _ in range(n):
        reach_limit.append(next(it))
        ride_cost.append(next(it))

    taxi_edges = [[] for _ in range(n)]
    for start in range(n):
        taxi_edges[start] = bounded_dijkstra(start, roads, reach_limit[start], n)

    best = [INF] * n
    best[x] = 0
    pq = [(0, x)]
    while pq:
        cost, v = heappop(pq)
        if cost != best[v]:
            continue
        if v == y:
            break
        nc = cost + ride_cost[v]
        for u in taxi_edges[v]:
            if nc < best[u]:
                best[u] = nc
                heappush(pq, (nc, u))

    print(best[y])

# CLAUSE: finish_program
main()
