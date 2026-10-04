# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        b = data[idx:idx + n]
        idx += n

        adj = [[] for _ in range(n + 1)]
        for x, y in zip(a, b):
            adj[x].append(y)
            adj[y].append(x)

        seen = [False] * (n + 1)
        m = 0

        for v in range(1, n + 1):
            if not seen[v]:
                stack = [v]
                seen[v] = True
                cnt = 0
                while stack:
                    u = stack.pop()
                    cnt += 1
                    for w in adj[u]:
                        if not seen[w]:
                            seen[w] = True
                            stack.append(w)
                m += cnt // 2

        out.append(str(2 * m * (n - m)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
