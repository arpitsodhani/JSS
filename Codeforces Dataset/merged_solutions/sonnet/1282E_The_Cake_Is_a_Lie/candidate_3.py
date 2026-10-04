# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def add_edge(counts, x, y):
    if x > y:
        x, y = y, x
    key = (x, y)
    counts[key] = counts.get(key, 0) + 1

def polygon_from_triangles(n, tris):
    if n == 3:
        return tris[0]

    counts = {}
    for tri in tris:
        a, b, c = tri
        add_edge(counts, a, b)
        add_edge(counts, b, c)
        add_edge(counts, a, c)

    adj = [[] for _ in range(n + 1)]
    for edge in counts:
        if counts[edge] == 1:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)

    start = 1
    while not adj[start]:
        start += 1

    result = []
    prev = -1
    cur = start
    while cur != start or not result:
        result.append(cur)
        a, b = adj[cur]
        nxt = a if a != prev else b
        prev = cur
        cur = nxt

    return result

# CLAUSE: finish_program
def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = tokens[idx]
    idx += 1
    answers = []
    for _ in range(t):
        n = tokens[idx]
        idx += 1
        tris = []
        for _ in range(n - 2):
            tris.append((tokens[idx], tokens[idx + 1], tokens[idx + 2]))
            idx += 3
        answers.append(" ".join(map(str, polygon_from_triangles(n, tris))))
    print("\n".join(answers))

main()
