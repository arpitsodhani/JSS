# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
import heapq

INF = 10 ** 30

def dijkstra_roads(start, roads, n):
    dist = [INF] * n
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        d, v = heapq.heappop(heap)
        if d != dist[v]:
            continue
        
        for to, w in roads[v]:
            nd = d + w
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(heap, (nd, to))
    
    return dist

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
    
    limit = [0] * n
    cost = [0] * n
    for i in range(n):
        limit[i] = data[idx]
        cost[i] = data[idx + 1]
        idx += 2
    
    road_dist = []
    for i in range(n):
        road_dist.append(dijkstra_roads(i, roads, n))
    
    fare = [INF] * n
    fare[x] = 0
    heap = [(0, x)]
    
    while heap:
        cur, v = heapq.heappop(heap)
        if cur != fare[v]:
            continue
        if v == y:
            break
        
        for to in range(n):
            if fare[to] > cur + cost[v] and road_dist[v][to] <= limit[v]:
                fare[to] = cur + cost[v]
                heapq.heappush(heap, (fare[to], to))
    
    print(fare[y])

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
