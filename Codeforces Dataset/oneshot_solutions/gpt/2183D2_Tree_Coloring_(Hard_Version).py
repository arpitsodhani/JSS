import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []

    for _ in range(t):
        n = data[p]
        p += 1

        g = [[] for _ in range(n)]
        for _ in range(n - 1):
            u = data[p] - 1
            v = data[p + 1] - 1
            p += 2
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        parent[0] = -2
        order = [0]

        for v in order:
            for to in g[v]:
                if to != parent[v]:
                    parent[to] = v
                    depth[to] = depth[v] + 1
                    order.append(to)

        layers = [[] for _ in range(max(depth) + 1)]
        for i, d in enumerate(depth):
            layers[d].append(i)

        max_layer = max(len(x) for x in layers)
        max_children = 0
        for v in range(n):
            c = len(g[v])
            if v != 0:
                c -= 1
            if c > max_children:
                max_children = c

        k = max(max_layer, max_children + 1)
        color = [0] * n

        for layer in layers:
            m = len(layer)
            bad = []

            for i, v in enumerate(layer):
                color[v] = i + 1
                if parent[v] >= 0 and color[parent[v]] == i + 1:
                    bad.append(i)

            if m < k:
                if len(bad) == 1:
                    color[layer[bad[0]]] = m + 1
                elif len(bad) > 1:
                    vals = [color[layer[i]] for i in bad]
                    q = len(bad)
                    for i in range(q):
                        color[layer[bad[i]]] = vals[(i + 1) % q]
            else:
                if len(bad) == 1:
                    b = bad[0]
                    for j in range(m):
                        if j == b:
                            continue
                        v = layer[j]
                        if parent[v] < 0 or color[parent[v]] != b + 1:
                            color[layer[b]], color[v] = color[v], color[layer[b]]
                            break
                elif len(bad) > 1:
                    vals = [color[layer[i]] for i in bad]
                    q = len(bad)
                    for i in range(q):
                        color[layer[bad[i]]] = vals[(i + 1) % q]

        ops = [[] for _ in range(k)]
        for v, c in enumerate(color):
            ops[c - 1].append(v + 1)

        out.append(str(k))
        for op in ops:
            out.append(str(len(op)) + (" " + " ".join(map(str, op)) if op else ""))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
