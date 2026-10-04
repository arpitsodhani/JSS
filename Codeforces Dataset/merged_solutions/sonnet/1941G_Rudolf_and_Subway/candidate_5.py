import sys


# --- clause: read_input :: () -> list[tuple[int, list[tuple[int, int, int]], int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        m = raw[offset + 1]
        offset += 2
        edges = []
        for _ in range(m):
            edges.append((raw[offset], raw[offset + 1], raw[offset + 2]))
            offset += 3
        start = raw[offset]
        goal = raw[offset + 1]
        offset += 2
        cases.append((n, edges, start, goal))
    return cases


# --- clause: build_graph :: (n: int, edges: list[tuple[int, int, int]]) -> list[list[int]] ---
def build_graph(n, edges):
    lines = {}
    for u, v, colour in edges:
        if colour not in lines:
            lines[colour] = n + 1 + len(lines)
    adj = [[] for _ in range(n + 1 + len(lines))]
    for u, v, colour in edges:
        hub = lines[colour]
        adj[u].append(hub)
        adj[hub].append(u)
        adj[v].append(hub)
        adj[hub].append(v)
    return adj


# --- clause: count_lines :: (adj: list[list[int]], start: int, goal: int) -> int ---
def count_lines(adj, start, goal):
    dist = [-1] * len(adj)
    dist[start] = 0
    queue = [start]
    front = 0
    while front < len(queue):
        v = queue[front]
        front += 1
        if v == goal:
            break
        for u in adj[v]:
            if dist[u] < 0:
                dist[u] = dist[v] + 1
                queue.append(u)
    return dist[goal] // 2


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, edges, start, goal in read_input():
        adj = build_graph(n, edges)
        out.append(count_lines(adj, start, goal))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
