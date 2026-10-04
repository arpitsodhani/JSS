# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n, x, y = data[0], data[1], data[2]
        g = [[] for _ in range(n + 1)]

        idx = 3
        for _ in range(n - 1):
            a, b = data[idx], data[idx + 1]
            idx += 2
            g[a].append(b)
            g[b].append(a)

        parent = [0] * (n + 1)
        order = [x]
        parent[x] = -1

        for v in order:
            for to in g[v]:
                if to != parent[v]:
                    parent[to] = v
                    order.append(to)

        sub = [1] * (n + 1)
        for v in reversed(order):
            if parent[v] != -1:
                sub[parent[v]] += sub[v]

        cur = y
        while parent[cur] != x:
            cur = parent[cur]

        bad = (n - sub[cur]) * sub[y]
        print(n * (n - 1) - bad)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
