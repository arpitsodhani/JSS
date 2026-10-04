# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def calc(vals):
    vals.sort(reverse=True)
    res = 1
    for i, x in enumerate(vals):
        y = x + i
        if y > res:
            res = y
    return res

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    g = [[] for _ in range(n + 1)]
    p = 1
    for _ in range(n - 1):
        u = data[p]
        v = data[p + 1]
        p += 2
        g[u].append(v)
        g[v].append(u)

    parent = [0] * (n + 1)
    order = [1]
    parent[1] = -1
    for u in order:
        for v in g[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)

    down = [1] * (n + 1)
    for u in reversed(order):
        vals = []
        for v in g[u]:
            if v != parent[u]:
                vals.append(down[v])
        down[u] = calc(vals)

    up = [1] * (n + 1)
    ans = 0

    for u in order:
        arr = []
        for v in g[u]:
            if v == parent[u]:
                arr.append((up[u], v))
            else:
                arr.append((down[v], v))

        arr.sort(reverse=True)
        d = len(arr)

        if d:
            cur = max(d, arr[0][0] + d - 1)
            best = arr[0][0]
            for i in range(1, d):
                val = best + arr[i][0] + i - 1
                if val > cur:
                    cur = val
            if cur > ans:
                ans = cur

        pref = [0] * (d + 1)
        for i in range(d):
            x = arr[i][0] + i
            pref[i + 1] = pref[i] if pref[i] > x else x

        suf = [0] * (d + 1)
        for i in range(d - 1, -1, -1):
            x = arr[i][0] + i
            suf[i] = suf[i + 1] if suf[i + 1] > x else x

        for i, (_, v) in enumerate(arr):
            if v != parent[u]:
                x = pref[i]
                y = suf[i + 1] - 1
                up[v] = max(1, x, y)

    if p + 2 < len(data):
        a, b = data[p], data[p + 1]
        sys.stdout.write(f"{ans}\n! {a} {b}\n")
    else:
        sys.stdout.write(str(ans) + "\n")

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
