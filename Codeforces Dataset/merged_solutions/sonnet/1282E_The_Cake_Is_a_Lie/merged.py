# Clause setup_environment [Confidence: 0.60]
import sys


# Clause solve_logic [Confidence: 0.40]
def solve_one(lines, pos):
    n = int(lines[pos])
    pos += 1
    triangles = []
    for _ in range(n - 2):
        triangles.append(tuple(map(int, lines[pos].split())))
        pos += 1

    if n == 3:
        return " ".join(map(str, triangles[0])), pos

    edge_count = defaultdict(int)
    for a, b, c in triangles:
        for u, v in ((a, b), (b, c), (a, c)):
            if u > v:
                u, v = v, u
            edge_count[(u, v)] += 1

    adj = defaultdict(list)
    for (u, v), count in edge_count.items():
        if count == 1:
            adj[u].append(v)
            adj[v].append(u)

    start = next(iter(adj))
    order = [start]
    prev = 0
    cur = start

    while True:
        nxt = adj[cur][0] if adj[cur][0] != prev else adj[cur][1]
        prev, cur = cur, nxt
        if cur == start:
            break
        order.append(cur)

    return " ".join(map(str, order)), pos


# Clause finish_program [Confidence: 0.60]
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


