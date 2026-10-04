# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, k = data[0], data[1]

    if n == 1:
        print(0)
        return

    g = [[] for _ in range(n)]
    idx = 2
    for _ in range(n - 1):
        a = data[idx] - 1
        b = data[idx + 1] - 1
        idx += 2
        g[a].append(b)
        g[b].append(a)

    if n == 2:
        print(1 if k >= 1 else 2)
        return

    root = 0
    for i in range(n):
        if len(g[i]) > 1:
            root = i
            break

    parent = [-2] * n
    parent[root] = -1
    order = [root]

    for v in order:
        for to in g[v]:
            if to != parent[v]:
                parent[to] = v
                order.append(to)

    ret = [0] * n
    ans = 0

    for v in reversed(order):
        vals = []
        for to in g[v]:
            if parent[to] == v:
                vals.append(ret[to] + 1)

        if not vals:
            ret[v] = 0
            continue

        vals.sort()
        while len(vals) >= 2 and vals[-1] + vals[-2] > k:
            ans += 1
            vals.pop()

        ret[v] = vals[-1]

    print(ans + 1)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
