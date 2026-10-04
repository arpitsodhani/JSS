# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1

        a = [0] + data[idx:idx + n]
        idx += n

        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = data[idx]
            v = data[idx + 1]
            idx += 2
            adj[u].append(v)
            adj[v].append(u)

        ans = [0] * (n + 1)
        mn = [0] * (n + 1)

        ans[1] = a[1]
        mn[1] = a[1]

        stack = [(1, 0)]
        while stack:
            v, p = stack.pop()
            for to in adj[v]:
                if to == p:
                    continue
                ans[to] = max(a[to], a[to] - mn[v])
                mn[to] = min(a[to], a[to] - ans[v])
                stack.append((to, v))

        out.append(" ".join(map(str, ans[1:])))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
