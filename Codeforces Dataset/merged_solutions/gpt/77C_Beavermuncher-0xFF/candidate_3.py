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
        k = [0] + data[1:1 + n]
        idx = 1 + n

        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            a = data[idx]
            b = data[idx + 1]
            idx += 2
            g[a].append(b)
            g[b].append(a)

        s = data[idx]

        parent = [0] * (n + 1)
        order = [s]
        parent[s] = -1

        for v in order:
            for u in g[v]:
                if u != parent[v]:
                    parent[u] = v
                    order.append(u)

        rem = [0] * (n + 1)
        matched = 0

        for v in reversed(order):
            need = 0
            for u in g[v]:
                if parent[u] == v:
                    need += rem[u]
            take = min(k[v], need)
            matched += take
            rem[v] = k[v] - take

        print(matched * 2)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
