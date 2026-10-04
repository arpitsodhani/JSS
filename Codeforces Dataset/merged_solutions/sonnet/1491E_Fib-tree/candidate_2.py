# CLAUSE: setup_environment
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

# CLAUSE: solve_logic
    sys.setrecursionlimit(300000)
    cut = [False] * max(1, n - 1)
    parent = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)
    size = [0] * (n + 1)

    def locate(root, idx):
        need1 = fib[idx - 1]
        need2 = fib[idx - 2]
        order = [root]
        parent[root] = 0
        parent_edge[root] = -1
        i = 0
        while i < len(order):
            node = order[i]
            i += 1
            for nxt, eid in g[node]:
                if cut[eid] or nxt == parent[node]:
                    continue
                parent[nxt] = node
                parent_edge[nxt] = eid
                order.append(nxt)
        for node in order[::-1]:
            total = 1
            for nxt, eid in g[node]:
                if not cut[eid] and parent[nxt] == node:
                    total += size[nxt]
            size[node] = total
            if node != root and (total == need1 or total == need2):
                return node
        return 0

    def valid(root, idx):
        if idx <= 1:
            return True
        node = locate(root, idx)
        if node == 0:
            return False
        part = size[node]
        cut[parent_edge[node]] = True
        if part == fib[idx - 1]:
            return valid(node, idx - 1) and valid(root, idx - 2)
        return valid(node, idx - 2) and valid(root, idx - 1)

    answer = valid(1, len(fib) - 1)

# CLAUSE: finish_program
    sys.stdout.write("YES" if answer else "NO")

if __name__ == "__main__":
    main()
