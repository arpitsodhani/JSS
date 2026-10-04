# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n = data[0]
        fib = [1, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])

        if fib[-1] != n:
            print("NO")
            return

        if n == 1:
            print("YES")
            return

        k0 = len(fib) - 1
        g = [[] for _ in range(n)]
        it = iter(data[1:])
        for i, (a, b) in enumerate(zip(it, it)):
            a -= 1
            b -= 1
            g[a].append((b, i))
            g[b].append((a, i))

        removed = [False] * (n - 1)
        parent = [-1] * n
        parent_edge = [-1] * n
        sz = [0] * n

        stack = [(0, n, k0)]

        while stack:
            root, total, k = stack.pop()
            if total == 1:
                continue

            need1 = fib[k - 1]
            need2 = fib[k - 2]

            order = []
            dfs = [root]
            parent[root] = -2
            parent_edge[root] = -1

            while dfs:
                v = dfs.pop()
                order.append(v)
                for to, eid in g[v]:
                    if removed[eid] or to == parent[v]:
                        continue
                    parent[to] = v
                    parent_edge[to] = eid
                    dfs.append(to)

            cut_node = -1
            cut_size = -1

            for v in reversed(order):
                s = 1
                for to, eid in g[v]:
                    if removed[eid] or parent[to] != v:
                        continue
                    s += sz[to]
                sz[v] = s
                if v != root and (s == need1 or s == need2):
                    cut_node = v
                    cut_size = s

            if cut_node == -1:
                print("NO")
                return

            removed[parent_edge[cut_node]] = True

            if cut_size == need1:
                stack.append((cut_node, need1, k - 1))
                stack.append((root, need2, k - 2))
            else:
                stack.append((cut_node, need2, k - 2))
                stack.append((root, need1, k - 1))

        print("YES")

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
