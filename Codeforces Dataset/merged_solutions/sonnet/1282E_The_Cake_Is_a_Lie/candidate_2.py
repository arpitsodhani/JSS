# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        ans, pos = solve_one(data, pos)
        out.append(ans)
    sys.stdout.write("\n".join(out))

main()
