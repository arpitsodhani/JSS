# Clause setup_environment [Confidence: 0.80]
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


# Clause solve_logic [Confidence: 0.80]
def main():
    raw = sys.stdin.buffer.read().split()
    pos = 0
    n = int(raw[pos])
    m = int(raw[pos + 1])
    pos += 2
    start = int(raw[pos]) - 1
    finish = int(raw[pos + 1]) - 1
    pos += 2

    adjacency = [[] for _ in range(n)]
    for _ in range(m):
        a = int(raw[pos]) - 1
        b = int(raw[pos + 1]) - 1
        c = int(raw[pos + 2])
        pos += 3
        adjacency[a].append((b, c))
        adjacency[b].append((a, c))

    taxis = []
    for _ in range(n):
        taxis.append((int(raw[pos]), int(raw[pos + 1])))
        pos += 2

    can_go = []
    for city in range(n):
        radius, fare = taxis[city]
        dist = road_distances(city, adjacency)
        can_go.append([i for i, d in enumerate(dist) if d <= radius])

    answer = [INF] * n
    answer[start] = 0
    heap = [(0, start)]
    while heap:
        paid, city = heapq.heappop(heap)
        if paid != answer[city]:
            continue
        if city == finish:
            break
        ride_price = taxis[city][1]
        new_paid = paid + ride_price
        for nxt in can_go[city]:
            if new_paid < answer[nxt]:
                answer[nxt] = new_paid
                heapq.heappush(heap, (new_paid, nxt))

    sys.stdout.write(str(answer[finish]))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


