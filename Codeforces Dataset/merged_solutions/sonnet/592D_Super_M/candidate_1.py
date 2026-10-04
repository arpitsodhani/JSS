import sys


# --- clause: read_input :: () -> tuple[int, list[list[int]], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    adj = [[] for _ in range(n + 1)]
    pos = 2
    for _ in range(n - 1):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
    return n, adj, data[pos:pos + m]


# --- clause: trim_tree :: (n: int, adj: list[list[int]], marked: list[int]) -> list[bool] ---
def trim_tree(n, adj, marked):
    keep = [False] * (n + 1)
    for v in marked:
        keep[v] = True
    degree = [len(adj[v]) for v in range(n + 1)]
    alive = [True] * (n + 1)
    queue = []
    for v in range(1, n + 1):
        if degree[v] <= 1 and not keep[v]:
            queue.append(v)
    head = 0
    while head < len(queue):
        v = queue[head]
        head += 1
        if keep[v]:
            continue
        alive[v] = False
        for u in adj[v]:
            if alive[u]:
                degree[u] -= 1
                if degree[u] <= 1 and not keep[u]:
                    queue.append(u)
    return alive


# --- clause: walk_from :: (n: int, adj: list[list[int]], alive: list[bool], start: int) -> list[int] ---
def walk_from(n, adj, alive, start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    order = [start]
    head = 0
    while head < len(order):
        v = order[head]
        head += 1
        for u in adj[v]:
            if alive[u] and dist[u] < 0:
                dist[u] = dist[v] + 1
                order.append(u)
    return dist


# --- clause: plan_trip :: (n: int, adj: list[list[int]], alive: list[bool], marked: list[int]) -> tuple[int, int] ---
def plan_trip(n, adj, alive, marked):
    edges = 0
    for v in range(1, n + 1):
        if not alive[v]:
            continue
        for u in adj[v]:
            if alive[u] and u > v:
                edges += 1
    first = marked[0]
    from_first = walk_from(n, adj, alive, first)
    far = first
    for v in marked:
        if from_first[v] > from_first[far] or (from_first[v] == from_first[far] and v < far):
            far = v
    from_far = walk_from(n, adj, alive, far)
    other = far
    for v in marked:
        if from_far[v] > from_far[other] or (from_far[v] == from_far[other] and v < other):
            other = v
    span = from_far[other]
    from_other = walk_from(n, adj, alive, other)
    start = 0
    for v in marked:
        reach = from_far[v] if from_far[v] > from_other[v] else from_other[v]
        if reach == span and (start == 0 or v < start):
            start = v
    return start, 2 * edges - span


# --- clause: main :: () -> None ---
def main():
    n, adj, marked = read_input()
    alive = trim_tree(n, adj, marked)
    start, time = plan_trip(n, adj, alive, marked)
    sys.stdout.write("%d\n%d\n" % (start, time))


if __name__ == "__main__":
    main()
