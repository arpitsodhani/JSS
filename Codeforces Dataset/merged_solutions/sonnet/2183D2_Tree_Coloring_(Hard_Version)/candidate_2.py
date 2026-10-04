# CLAUSE: setup_environment
import sys
from collections import deque

def choose_colors(vertices, parent_col, limit):
    count = len(vertices)
    chosen = list(range(1, count + 1))
    blocked = [parent_col[v] for v in vertices]
    if count < limit:
        extra = count + 1
        for i in range(count):
            if chosen[i] == blocked[i]:
                chosen[i] = extra
                extra = blocked[i]
        return chosen
    first = 0
    other = -1
    for i in range(1, count):
        if blocked[i] != blocked[first]:
            other = i
            break
    for i in range(count):
        if chosen[i] == blocked[i]:
            j = first if blocked[first] != blocked[i] else other
            chosen[i], chosen[j] = chosen[j], chosen[i]
    return chosen

# CLAUSE: solve_logic
def solve_one(n, pairs):
    graph = [[] for _ in range(n + 1)]
    for a, b in pairs:
        graph[a].append(b)
        graph[b].append(a)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    levels = []
    q = deque([1])
    parent[1] = -1

    while q:
        v = q.popleft()
        d = depth[v]
        if d == len(levels):
            levels.append([])
        levels[d].append(v)
        for u in graph[v]:
            if u != parent[v]:
                parent[u] = v
                depth[u] = d + 1
                q.append(u)

    width = 0
    for level in levels:
        if len(level) > width:
            width = len(level)

    need = width
    for level in levels[1:]:
        if len(level) == width:
            base = parent[level[0]]
            ok = True
            for v in level:
                if parent[v] != base:
                    ok = False
                    break
            if ok:
                need += 1
                break

    color = [0] * (n + 1)
    color[1] = 1
    groups = [[] for _ in range(need + 1)]
    groups[1].append(1)

    for level in levels[1:]:
        parent_col = [0] * (n + 1)
        for v in level:
            parent_col[v] = color[parent[v]]
        got = choose_colors(level, parent_col, need)
        for v, c in zip(level, got):
            color[v] = c
            groups[c].append(v)

    ans = [str(need)]
    for c in range(1, need + 1):
        group = groups[c]
        ans.append(str(len(group)) + (" " + " ".join(map(str, group)) if group else ""))
    return ans

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    pos = 1
    out = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        edges = []
        for _ in range(n - 1):
            edges.append((data[pos], data[pos + 1]))
            pos += 2
        out.extend(solve_one(n, edges))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
