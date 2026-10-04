# Clause setup_environment [Confidence: 0.80]
import sys

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n = values[0]
    fib = [1, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    if fib[-1] != n:
        sys.stdout.write("NO")
        return
    g = [[] for _ in range(n + 1)]
    p = 1
    for eid in range(n - 1):
        u = values[p]
        v = values[p + 1]
        p += 2
        g[u].append((v, eid))
        g[v].append((u, eid))


# Clause solve_logic [Confidence: 0.80]
    removed = [0] * max(1, n - 1)
    par = [0] * (n + 1)
    pedge = [-1] * (n + 1)
    sub = [0] * (n + 1)
    sys.setrecursionlimit(300000)

    def build_order(start):
        order = []
        stack = [start]
        par[start] = 0
        pedge[start] = -1
        while stack:
            v = stack.pop()
            order.append(v)
            for to, eid in adj[v]:
                if removed[eid] == 0 and to != par[v]:
                    par[to] = v
                    pedge[to] = eid
                    stack.append(to)
        return order

    def split_vertex(start, k):
        left = fib[k - 1]
        right = fib[k - 2]
        order = build_order(start)
        for v in reversed(order):
            cur = 1
            for to, eid in adj[v]:
                if removed[eid] == 0 and par[to] == v:
                    cur += sub[to]
            sub[v] = cur
            if v != start and (cur == left or cur == right):
                return v
        return -1

    def decompose(start, k):
        if k < 2:
            return True
        found = split_vertex(start, k)
        if found < 0:
            return False
        removed[pedge[found]] = 1
        got = sub[found]
        if got == fib[k - 2]:
            return decompose(found, k - 2) and decompose(start, k - 1)
        return decompose(found, k - 1) and decompose(start, k - 2)

    ok = decompose(1, pos)


# Clause finish_program [Confidence: 0.80]
    print("YES" if ok else "NO")

if __name__ == "__main__":
    main()


