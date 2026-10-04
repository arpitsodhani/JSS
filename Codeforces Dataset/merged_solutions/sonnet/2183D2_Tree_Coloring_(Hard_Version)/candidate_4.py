# CLAUSE: setup_environment
import sys
from collections import deque

def remap_colors(level, previous, total):
    m = len(level)
    ans = list(range(1, m + 1))
    bad = []
    for node in level:
        bad.append(previous[node])
    if m < total:
        spare = m + 1
        i = 0
        while i < m:
            if ans[i] == bad[i]:
                ans[i], spare = spare, bad[i]
            i += 1
        return ans
    first = 0
    second = -1
    i = 1
    while i < m:
        if bad[i] != bad[first]:
            second = i
            break
        i += 1
    i = 0
    while i < m:
        if ans[i] == bad[i]:
            j = first
            if bad[first] == bad[i]:
                j = second
            ans[i], ans[j] = ans[j], ans[i]
        i += 1
    return ans

# CLAUSE: solve_logic
def build_answer(n, edge_list):
    g = [[] for _ in range(n + 1)]
    for e in edge_list:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])

    par = [0] * (n + 1)
    dep = [-1] * (n + 1)
    levels = []
    que = deque()
    que.append(1)
    par[1] = -1
    dep[1] = 0

    while que:
        v = que.popleft()
        dv = dep[v]
        if len(levels) <= dv:
            levels.append([])
        levels[dv].append(v)
        for to in g[v]:
            if dep[to] == -1:
                dep[to] = dv + 1
                par[to] = v
                que.append(to)

    max_size = 1
    for lv in levels:
        max_size = max(max_size, len(lv))

    ops = max_size
    d = 1
    while d < len(levels):
        lv = levels[d]
        if len(lv) == max_size:
            same = True
            root_parent = par[lv[0]]
            for node in lv:
                if par[node] != root_parent:
                    same = False
                    break
            if same:
                ops += 1
                break
        d += 1

    node_color = [0] * (n + 1)
    node_color[1] = 1
    buckets = [[] for _ in range(ops + 1)]
    buckets[1] = [1]
    old = [0] * (n + 1)

    for lv in levels[1:]:
        for node in lv:
            old[node] = node_color[par[node]]
        new_colors = remap_colors(lv, old, ops)
        for node, c in zip(lv, new_colors):
            node_color[node] = c
            buckets[c].append(node)

    out = [str(ops)]
    for c in range(1, ops + 1):
        bucket = buckets[c]
        out.append(" ".join([str(len(bucket))] + [str(x) for x in bucket]))
    return out

# CLAUSE: finish_program
def main():
    raw = sys.stdin.buffer.read().split()
    p = 0
    t = int(raw[p])
    p += 1
    all_lines = []
    for _ in range(t):
        n = int(raw[p])
        p += 1
        edges = []
        for _ in range(n - 1):
            a = int(raw[p])
            b = int(raw[p + 1])
            p += 2
            edges.append((a, b))
        all_lines.extend(build_answer(n, edges))
    sys.stdout.write("\n".join(all_lines))

if __name__ == "__main__":
    main()
