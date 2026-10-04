# CLAUSE: setup_environment
import sys

def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    if not data:
        return
    n = data[0]
    fib = [1, 1]
    while fib[-1] < n:
        fib += [fib[-1] + fib[-2]]
    if n not in fib:
        sys.stdout.write("NO")
        return
    k0 = max(i for i, x in enumerate(fib) if x == n)
    graph = [[] for _ in range(n + 1)]
    for eid, j in enumerate(range(1, len(data), 2)):
        u = data[j]
        v = data[j + 1]
        graph[u].append((v, eid))
        graph[v].append((u, eid))

# CLAUSE: solve_logic
    blocked = set()
    up = [0] * (n + 1)
    via = [-1] * (n + 1)
    count = [0] * (n + 1)
    sys.setrecursionlimit(300000)

    def scan(root, k):
        want = (fib[k - 1], fib[k - 2])
        stack = [(root, 0, -1, 0)]
        seen = []
        while stack:
            v, p, e, state = stack.pop()
            if state == 0:
                up[v] = p
                via[v] = e
                seen.append(v)
                stack.append((v, p, e, 1))
                for to, edge_id in graph[v]:
                    if edge_id not in blocked and to != p:
                        stack.append((to, v, edge_id, 0))
            else:
                total = 1
                for to, edge_id in graph[v]:
                    if edge_id not in blocked and up[to] == v:
                        total += count[to]
                count[v] = total
                if v != root and total in want:
                    return v
        return -1

    def dfs(root, k):
        if k <= 1:
            return True
        node = scan(root, k)
        if node == -1:
            return False
        blocked.add(via[node])
        if count[node] == fib[k - 1]:
            first = k - 1
            second = k - 2
        else:
            first = k - 2
            second = k - 1
        return dfs(node, first) and dfs(root, second)

    good = dfs(1, k0)

# CLAUSE: finish_program
    sys.stdout.write("YES\n" if good else "NO\n")

if __name__ == "__main__":
    main()
