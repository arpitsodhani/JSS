# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 1.00]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, h, t = data[:4]
    adj = [[] for _ in range(n + 1)]
    edges = []
    pos = 4

    for _ in range(m):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    mark = [0] * (n + 1)
    stamp = 0

    def attempt(u, v):
        nonlocal stamp
        if len(adj[u]) <= h or len(adj[v]) <= t:
            return None
        if len(adj[u]) + len(adj[v]) - 2 < h + t:
            return None

        stamp += 2
        first = stamp
        both = stamp + 1

        for x in adj[u]:
            if x != v:
                mark[x] = first

        tails = []
        shared = []

        for x in adj[v]:
            if x == u:
                continue
            if mark[x] == first:
                mark[x] = both
                shared.append(x)
            else:
                tails.append(x)

        heads = []
        for x in adj[u]:
            if x != v and mark[x] == first:
                heads.append(x)

        need_h = h - len(heads)
        if need_h < 0:
            need_h = 0
        need_t = t - len(tails)
        if need_t < 0:
            need_t = 0

        if need_h + need_t > len(shared):
            return None

        return heads[:h] + shared[:need_h], tails[:t] + shared[need_h:need_h + need_t]

    for u, v in edges:
        result = attempt(u, v)
        if result is not None:
            heads, tails = result
            sys.stdout.write("YES\n{} {}\n{}\n{}\n".format(u, v, " ".join(map(str, heads)), " ".join(map(str, tails))))
            return

        result = attempt(v, u)
        if result is not None:
            heads, tails = result
            sys.stdout.write("YES\n{} {}\n{}\n{}\n".format(v, u, " ".join(map(str, heads)), " ".join(map(str, tails))))
            return

    sys.stdout.write("NO\n")


# Clause finish_program [Confidence: 0.80]
if __name__ == "__main__":
    main()


