# CLAUSE: setup_environment
import sys

def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    fib = [1, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    pos = -1
    for i, x in enumerate(fib):
        if x == n:
            pos = i
            break
    if pos < 0:
        print("NO")
        return
    adj = [[] for _ in range(n + 1)]
    it = 1
    edge_no = 0
    while edge_no < n - 1:
        a = int(raw[it])
        b = int(raw[it + 1])
        it += 2
        adj[a].append((b, edge_no))
        adj[b].append((a, edge_no))
        edge_no += 1

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
    print("YES" if ok else "NO")

if __name__ == "__main__":
    main()
