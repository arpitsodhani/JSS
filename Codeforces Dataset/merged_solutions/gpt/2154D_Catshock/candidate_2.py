# CLAUSE: root_target_tree
import sys

def build_answer(n, pairs):
    adj = [[] for _ in range(n + 1)]
    for u, v in pairs:
        adj[u].append(v)
        adj[v].append(u)

    par = [0] * (n + 1)
    dep = [0] * (n + 1)
    seen = [False] * (n + 1)
    seen[n] = True
    order = []
    st = [(n, 0)]
    while st:
        v, i = st.pop()
        if i == 0:
            order.append(v)
        if i < len(adj[v]):
            st.append((v, i + 1))
            to = adj[v][i]
            if not seen[to]:
                seen[to] = True
                par[to] = v
                dep[to] = dep[v] + 1
                st.append((to, 0))

# CLAUSE: derive_escape_path
    path = []
    cur = 1
    while True:
        path.append(cur)
        if cur == n:
            break
        cur = par[cur]
    path_set = set(path)

# CLAUSE: partition_side_subtrees
    buckets = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        if v != n:
            buckets[dep[v]].append(v)
    deepest_first = []
    for d in range(n, -1, -1):
        off = []
        on = []
        for v in buckets[d]:
            if v in path_set:
                on.append(v)
            else:
                off.append(v)
        deepest_first.extend(off)
        deepest_first.extend(on)

# CLAUSE: schedule_safe_deletions
    res = []
    possible_color = dep[1] % 2
    for v in deepest_first:
        need_color = dep[v] % 2
        steps = 1 if possible_color == need_color else 2
        for _ in range(steps):

# CLAUSE: enforce_walk_progress
            res.append("1")
            possible_color ^= 1

# CLAUSE: maintain_reachable_frontier
        res.append(f"2 {v}")

# CLAUSE: finalize_target_arrival
    return res

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(it)
    parts = []
    for _ in range(t):
        n = next(it)
        pairs = [(next(it), next(it)) for _ in range(n - 1)]
        ans = build_answer(n, pairs)
        parts.append(str(len(ans)))
        parts += ans
    print("\n".join(parts))

main()
