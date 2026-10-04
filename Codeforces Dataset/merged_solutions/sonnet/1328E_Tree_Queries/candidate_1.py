import sys


# --- clause: read_input :: () -> tuple[int, list[tuple[int, int]], list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    edges = []
    pos = 2
    for _ in range(n - 1):
        edges.append((data[pos], data[pos + 1]))
        pos += 2
    queries = []
    for _ in range(m):
        k = data[pos]
        pos += 1
        queries.append(data[pos:pos + k])
        pos += k
    return n, edges, queries


# --- clause: euler_walk :: (n: int, edges: list[tuple[int, int]]) -> tuple[list[int], list[int], list[int], list[int]] ---
def euler_walk(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    parent[1] = 1
    timer = 0
    stack = [(1, 0)]
    while stack:
        v, state = stack.pop()
        if state:
            tout[v] = timer
            continue
        timer += 1
        tin[v] = timer
        stack.append((v, 1))
        for u in adj[v]:
            if u != parent[v] or v == 1:
                if u == parent[v] and v != 1:
                    continue
                if u == 1:
                    continue
                parent[u] = v
                depth[u] = depth[v] + 1
                stack.append((u, 0))
    return parent, depth, tin, tout


# --- clause: answer_query :: (spots: list[int], parent: list[int], depth: list[int], tin: list[int], tout: list[int]) -> bool ---
def answer_query(spots, parent, depth, tin, tout):
    marks = []
    for v in spots:
        marks.append(v if v == 1 else parent[v])
    deepest = marks[0]
    for v in marks:
        if depth[v] > depth[deepest]:
            deepest = v
    for v in marks:
        if not (tin[v] <= tin[deepest] and tout[deepest] <= tout[v]):
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    n, edges, queries = read_input()
    parent, depth, tin, tout = euler_walk(n, edges)
    out = []
    for spots in queries:
        out.append("YES" if answer_query(spots, parent, depth, tin, tout) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
