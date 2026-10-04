# CLAUSE: setup_environment
import sys
from bisect import bisect_left, insort

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    out = []
    for _ in range(t):
        n = data[pos]
        q = data[pos + 1]
        pos += 2

        parent = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
        for v in range(2, n + 1):
            p = data[pos]
            pos += 1
            parent[v] = p
            children[p].append(v)

        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = data[pos]
            pos += 1

        order = [1]
        for v in order:
            order.extend(children[v])

        dp = [0] * (n + 1)
        extra = [0] * (n + 1)
        for v in reversed(order):
            s = 0
            for c in children[v]:
                s += dp[c]
            if a[v] > s:
                extra[v] = a[v] - s
                dp[v] = a[v]
            else:
                dp[v] = s

        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        timer = 0
        stack = [(1, 0)]
        while stack:
            v, state = stack.pop()
            if state == 0:
                timer += 1
                tin[v] = timer
                stack.append((v, 1))
                for c in reversed(children[v]):
                    stack.append((c, 0))
            else:
                tout[v] = timer

        active = []
        for v in range(1, n + 1):
            if extra[v] > 0:
                active.append(tin[v])
        active.sort()
        by_time = [0] * (n + 1)
        for v in range(1, n + 1):
            by_time[tin[v]] = v

        ans = dp[1]
        out.append(str(ans))

        for _ in range(q):
            u = data[pos]
            x = data[pos + 1]
            pos += 2
            old = extra[u]
            base = a[u] - old
            new = x - base
            if new < 0:
                new = 0
            a[u] = x
            if new != old:
                extra[u] = new
                key = tin[u]
                if old == 0:
                    insort(active, key)
                elif new == 0:
                    active.pop(bisect_left(active, key))

                change = new - old
                if change > 0:
                    ans += change
                    need = change
                    limit = tin[u]
                    while True:
                        k = bisect_left(active, limit) - 1
                        if k < 0:
                            break
                        v = by_time[active[k]]
                        if tout[v] < tin[u]:
                            break
                        take = extra[v] if extra[v] < need else need
                        extra[v] -= take
                        ans -= take
                        need -= take
                        if extra[v] == 0:
                            active.pop(k)
                        if need == 0:
                            break
                else:
                    ans += change
            out.append(str(ans))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
