# CLAUSE: setup_environment
import sys
import heapq

INF = 10 ** 30

def road_distances(start, adjacency):
    n = len(adjacency)
    dist = [INF] * n
    dist[start] = 0
    queue = [(0, start)]
    pop = heapq.heappop
    push = heapq.heappush
    while queue:
        cur, node = pop(queue)
        if cur != dist[node]:
            continue
        for nxt, length in adjacency[node]:
            val = cur + length
            if val < dist[nxt]:
                dist[nxt] = val
                push(queue, (val, nxt))
    return dist

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
