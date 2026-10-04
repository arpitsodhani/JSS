# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import deque

    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, s = data[0], data[1], data[2]

    directed = [[] for _ in range(n + 1)]
    all_adj = [[] for _ in range(n + 1)]
    undirected_edges = []

    p = 3
    uid = 0
    for _ in range(m):
        t, u, v = data[p], data[p + 1], data[p + 2]
        p += 3
        if t == 1:
            directed[u].append(v)
            all_adj[u].append((v, -1, 1))
        else:
            undirected_edges.append((u, v))
            all_adj[u].append((v, uid, 1))
            all_adj[v].append((u, uid, -1))
            uid += 1

    k = len(undirected_edges)

    vis = [False] * (n + 1)
    ans_max = ['+'] * k
    q = deque([s])
    vis[s] = True
    cnt_max = 0

    while q:
        u = q.popleft()
        cnt_max += 1
        for v, eid, sign in all_adj[u]:
            if not vis[v]:
                vis[v] = True
                q.append(v)
                if eid != -1:
                    ans_max[eid] = '+' if sign == 1 else '-'

    vis = [False] * (n + 1)
    q = deque([s])
    vis[s] = True
    cnt_min = 0

    while q:
        u = q.popleft()
        cnt_min += 1
        for v in directed[u]:
            if not vis[v]:
                vis[v] = True
                q.append(v)

    ans_min = ['+'] * k
    for i, (u, v) in enumerate(undirected_edges):
        if vis[u] and not vis[v]:
            ans_min[i] = '-'
        else:
            ans_min[i] = '+'

    print(cnt_max)
    print(''.join(ans_max))
    print(cnt_min)
    print(''.join(ans_min))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
