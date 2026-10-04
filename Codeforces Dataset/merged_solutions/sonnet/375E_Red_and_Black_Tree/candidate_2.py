# CLAUSE: setup_environment
import sys

INF = 10 ** 30
NEG = -10 ** 18

# CLAUSE: solve_logic
def prune(states):
    if not states:
        return {}
    vals = sorted({b for _, b in states})
    place = {v: i for i, v in enumerate(vals)}
    tree = [NEG] * (len(vals) + 1)

    def put(i, val):
        i += 1
        while i <= len(vals):
            if val > tree[i]:
                tree[i] = val
            i += i & -i

    def get(i):
        i += 1
        ans = NEG
        while i:
            if tree[i] > ans:
                ans = tree[i]
            i -= i & -i
        return ans

    out = {}
    triples = [(a, b, c) for (a, b), c in states.items()]
    triples.sort(key=lambda z: (z[0], z[1], -z[2]))
    for d, need, score in triples:
        p = place[need]
        if get(p) >= score:
            continue
        out[(d, need)] = score
        put(p, score)
    return out

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = 0
    n, x = data[it], data[it + 1]
    it += 2
    color = [0] + data[it:it + n]
    it += n
    total = sum(color)
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, w = data[it], data[it + 1], data[it + 2]
        it += 3
        graph[a].append((b, w))
        graph[b].append((a, w))

    parent = [0] * (n + 1)
    parent[1] = -1
    order = [1]
    for v in order:
        for to, _ in graph[v]:
            if to != parent[v]:
                parent[to] = v
                order.append(to)

    dp = [None] * (n + 1)
    size = [0] * (n + 1)

    for v in reversed(order):
        cur = [{} for _ in range(min(total, 1) + 1)]
        cur[0][(INF, 0)] = 0
        if total:
            cur[1][(0, -1)] = color[v]
        size[v] = 1

        for to, w in graph[v]:
            if parent[to] != v:
                continue
            child = []
            for layer in dp[to]:
                shifted = {}
                for (d, need), score in layer.items():
                    nd = d + w if d != INF and d + w <= x else INF
                    if need == -1:
                        nn = -1
                    else:
                        nn = need + w
                        if nn > x:
                            continue
                    key = (nd, nn)
                    if score > shifted.get(key, NEG):
                        shifted[key] = score
                child.append(shifted)

            lim = min(total, size[v] + size[to])
            nxt = [{} for _ in range(lim + 1)]
            for c1, s1 in enumerate(cur):
                if not s1:
                    continue
                for c2, s2 in enumerate(child):
                    if c1 + c2 > lim or not s2:
                        continue
                    dest = nxt[c1 + c2]
                    for (d1, n1), sc1 in s1.items():
                        for (d2, n2), sc2 in s2.items():
                            nd = d1 if d1 < d2 else d2
                            r1 = n1 if n1 != -1 and (d2 == INF or n1 + d2 > x) else -1
                            r2 = n2 if n2 != -1 and (d1 == INF or n2 + d1 > x) else -1
                            nn = r1 if r1 > r2 else r2
                            val = sc1 + sc2
                            key = (nd, nn)
                            if val > dest.get(key, NEG):
                                dest[key] = val
            cur = [prune(s) for s in nxt]
            size[v] += size[to]
        dp[v] = cur

    ans = NEG
    if total < len(dp[1]):
        for (_, need), score in dp[1][total].items():
            if need == -1 and score > ans:
                ans = score
    sys.stdout.write(str(-1 if ans == NEG else total - ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
