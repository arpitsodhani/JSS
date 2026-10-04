# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        input = sys.stdin.readline
        n, m = map(int, input().split())

        parent_dsu = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent_dsu[x] != x:
                parent_dsu[x] = parent_dsu[parent_dsu[x]]
                x = parent_dsu[x]
            return x

        tree = [[] for _ in range(n + 1)]
        extra = []

        for i in range(1, m + 1):
            u, v = map(int, input().split())
            ru, rv = find(u), find(v)
            if ru != rv:
                if size[ru] < size[rv]:
                    ru, rv = rv, ru
                parent_dsu[rv] = ru
                size[ru] += size[rv]
                tree[u].append(v)
                tree[v].append(u)
            else:
                extra.append((u, v))

        LOG = (n + 1).bit_length()
        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)

        timer = 0
        stack = [(1, 0, 0)]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                timer += 1
                tin[u] = timer
                up[0][u] = p
                stack.append((u, p, 1))
                for v in reversed(tree[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        for j in range(1, LOG):
            prev = up[j - 1]
            cur = up[j]
            for i in range(1, n + 1):
                cur[i] = prev[prev[i]]

        def is_ancestor(a, b):
            return tin[a] <= tin[b] <= tout[a]

        def lca(a, b):
            if is_ancestor(a, b):
                return a
            if is_ancestor(b, a):
                return b
            x = a
            for j in range(LOG - 1, -1, -1):
                y = up[j][x]
                if y and not is_ancestor(y, b):
                    x = y
            return up[0][x]

        def jump(x, d):
            bit = 0
            while d:
                if d & 1:
                    x = up[bit][x]
                d >>= 1
                bit += 1
            return x

        def next_towards(a, b):
            c = lca(a, b)
            if c != a:
                return up[0][a]
            return jump(b, depth[b] - depth[a] - 1)

        diff = [0] * (n + 3)

        def add_range(l, r, val):
            diff[l] += val
            diff[r + 1] -= val

        def add_component(x, y):
            if up[0][y] == x:
                add_range(1, n, 1)
                add_range(tin[y], tout[y], -1)
            else:
                add_range(tin[x], tout[x], 1)

        for u, v in extra:
            a = next_towards(u, v)
            b = next_towards(v, u)
            add_component(u, a)
            add_component(v, b)

        need = len(extra)
        vals = [0] * (n + 1)
        cur = 0
        for i in range(1, n + 1):
            cur += diff[i]
            vals[i] = cur

        ans = ['0'] * n
        for v in range(1, n + 1):
            if vals[tin[v]] == need:
                ans[v - 1] = '1'

        print(''.join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
