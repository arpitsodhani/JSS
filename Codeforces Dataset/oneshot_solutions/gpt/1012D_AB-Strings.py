import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s1, s2 = data[0], data[1]

    color = [0]
    val = [0]
    nxt = [0]
    head = [0, 0]
    ln = [0, 0]

    def new_node(c, v, n):
        color.append(c)
        val.append(v)
        nxt.append(n)
        return len(color) - 1

    def build(f, s):
        p = new_node(0 if s[0] == 'a' else 1, 1, 0)
        head[f] = p
        ln[f] = 1
        for ch in s[1:]:
            c = 0 if ch == 'a' else 1
            if c == color[p]:
                val[p] += 1
            else:
                q = new_node(c, 1, 0)
                nxt[p] = q
                p = q
                ln[f] += 1

    def div0(x, y):
        return x // y if x >= 0 else -((-x) // y)

    def f0(x, a, b):
        return abs((a - 2 * x - 1) - (b + 2 * x))

    def f1(x, a, b):
        return abs((a - 2 * x) - (b + 2 * x - 2))

    def f2(x, a, b):
        return abs((a - 2 * x - 1) - (b + 2 * x - 1))

    def get_len(f):
        p = head[f]
        res = 0
        while p:
            res += 1
            p = nxt[p]
        return res

    build(0, s1)
    build(1, s2)

    L, R = 0, 1
    ans = []

    while max(ln[L], ln[R]) > 1:
        if ln[L] < ln[R]:
            L, R = R, L

        if color[head[L]] == color[head[R]] and ln[R] > 1 and ln[L] > 2:
            a, b = ln[L], ln[R]
            x1 = div0(a - b + 2, 4)
            x2 = x1 + 1
            x = x1 if f1(x1, a, b) <= f1(x2, a, b) else x2
            x = max(1, min(x, a // 2))

            total = val[head[L]]
            p = head[L]
            for _ in range(1, x * 2):
                p = nxt[p]
                total += val[p]

            cur = [0, 0]
            cur[L] = total
            cur[R] = val[head[R]]
            ans.append(cur)

            hL, hR = head[L], head[R]
            head[L] = nxt[p]
            val[head[L]] += val[hR]
            head[R] = hL
            nxt[p] = nxt[nxt[hR]]
            val[p] += val[nxt[hR]]
            ln[L] -= x * 2
            ln[R] += x * 2 - 2

        elif color[head[L]] == color[head[R]]:
            a, b = ln[L], ln[R]
            x1 = div0(a - b - 1, 4)
            x2 = x1 + 1
            x = x1 if f0(x1, a, b) <= f0(x2, a, b) else x2
            x = min(x, (a - 1) // 2)

            total = val[head[L]]
            p = head[L]
            for _ in range(1, x * 2 + 1):
                p = nxt[p]
                total += val[p]

            cur = [0, 0]
            cur[L] = total
            ans.append(cur)

            head[R], head[L] = head[L], head[R]
            nxt[p], head[L] = head[L], nxt[p]
            val[p] += val[nxt[p]]
            nxt[p] = nxt[nxt[p]]

            ln[L] = get_len(L) if ln[L] < 3 else ln[L] - (x * 2 + 1)
            ln[R] = get_len(R) if ln[R] < 3 else ln[R] + x * 2

        else:
            a, b = ln[L], ln[R]
            x1 = div0(a - b - 1, 4)
            x2 = x1 + 1
            x = x1 if f2(x1, a, b) <= f2(x2, a, b) else x2
            x = min(x, (a - 1) // 2)

            total = val[head[L]]
            p = head[L]
            for _ in range(1, x * 2 + 1):
                p = nxt[p]
                total += val[p]

            cur = [0, 0]
            cur[L] = total
            cur[R] = val[head[R]]
            ans.append(cur)

            val[head[R]] += val[nxt[p]]
            val[p] += val[nxt[head[R]]]
            nxt[head[R]], nxt[p] = nxt[p], nxt[head[R]]
            nxt[head[R]] = nxt[nxt[head[R]]]
            nxt[p] = nxt[nxt[p]]
            head[L], head[R] = head[R], head[L]

            ln[L] = get_len(L) if ln[L] < 3 else ln[L] - (x * 2 + 1)
            ln[R] = get_len(R) if ln[R] < 3 else ln[R] + (x * 2 - 1)

    out = [str(len(ans))]
    out += [f"{a} {b}" for a, b in ans]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
