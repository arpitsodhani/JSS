import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1

        children = [[] for _ in range(n)]
        for v in range(1, n):
            p = data[idx] - 1
            idx += 1
            children[p].append(v)

        l = [0] * n
        r = [0] * n
        for i in range(n):
            l[i] = data[idx]
            r[i] = data[idx + 1]
            idx += 2

        order = []
        stack = [0]
        while stack:
            v = stack.pop()
            order.append(v)
            stack.extend(children[v])

        val = [0] * n
        ans = 0

        for v in reversed(order):
            s = 0
            for u in children[v]:
                s += val[u]

            if s < l[v]:
                ans += 1
                val[v] = r[v]
            else:
                val[v] = min(s, r[v])

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
