import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2

        edges = []
        a = [0] * n

        for _ in range(m):
            v = data[idx] - 1
            u = data[idx + 1] - 1
            w = data[idx + 2]
            idx += 3
            edges.append((v, u, w))
            if w > a[v]:
                a[v] = w
            if w > a[u]:
                a[u] = w

        ok = True
        for v, u, w in edges:
            if min(a[v], a[u]) != w:
                ok = False
                break

        if ok:
            out.append("YES")
            out.append(" ".join(map(str, a)))
        else:
            out.append("NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
