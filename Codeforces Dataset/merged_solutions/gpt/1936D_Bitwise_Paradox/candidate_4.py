# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    INF = 10**30

    def solve_case(n, v, a, b, queries):
        def leaf(i):
            x = b[i]
            y = a[i]
            return ([(x, y)], [(x, y)], x, y, y if x >= v else INF)

        def cross_ans(suf, pref):
            i = j = 0
            os = op = 0
            ns = len(suf)
            np = len(pref)
            while i < ns or j < np:
                if j == np or (i < ns and suf[i][1] <= pref[j][1]):
                    t = suf[i][1]
                else:
                    t = pref[j][1]
                while i < ns and suf[i][1] <= t:
                    os |= suf[i][0]
                    i += 1
                while j < np and pref[j][1] <= t:
                    op |= pref[j][0]
                    j += 1
                if (os | op) >= v:
                    return t
            return INF

        def add_pair(lst, o, val):
            if lst and lst[-1][0] == o:
                if val < lst[-1][1]:
                    lst[-1] = (o, val)
            else:
                lst.append((o, val))

        def merge(x, y):
            if x is None:
                return y
            if y is None:
                return x

            xp, xs, xo, xa, xb = x
            yp, ys, yo, ya, yb = y

            full_o = xo | yo
            full_a = xa if xa >= ya else ya

            pref = xp.copy()
            for o, val in yp:
                nv = xa if xa >= val else val
                add_pair(pref, xo | o, nv)

            suff = ys.copy()
            for o, val in xs:
                nv = ya if ya >= val else val
                add_pair(suff, yo | o, nv)

            best = xb if xb <= yb else yb
            c = cross_ans(xs, yp)
            if c < best:
                best = c

            return (pref, suff, full_o, full_a, best)

        size = 1
        while size < n:
            size <<= 1

        tree = [None] * (2 * size)
        for i in range(n):
            tree[size + i] = leaf(i)
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i << 1], tree[i << 1 | 1])

        out = []

        for query in queries:
            if query[0] == 1:
                _, idx, x = query
                idx -= 1
                b[idx] = x
                p = size + idx
                tree[p] = leaf(idx)
                p >>= 1
                while p:
                    tree[p] = merge(tree[p << 1], tree[p << 1 | 1])
                    p >>= 1
            else:
                _, l, r = query
                l += size - 1
                r += size - 1
                left = None
                right = None
                while l <= r:
                    if l & 1:
                        left = merge(left, tree[l])
                        l += 1
                    if not (r & 1):
                        right = merge(tree[r], right)
                        r -= 1
                    l >>= 1
                    r >>= 1
                res = merge(left, right)
                ans = res[4]
                out.append(str(ans if ans < INF else -1))

        return " ".join(out)

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        ptr = 0
        t = data[ptr]
        ptr += 1
        answers = []

        for _ in range(t):
            n = data[ptr]
            v = data[ptr + 1]
            ptr += 2

            a = data[ptr:ptr + n]
            ptr += n

            b = data[ptr:ptr + n]
            ptr += n

            q = data[ptr]
            ptr += 1

            queries = []
            for _ in range(q):
                typ = data[ptr]
                if typ == 1:
                    queries.append((1, data[ptr + 1], data[ptr + 2]))
                else:
                    queries.append((2, data[ptr + 1], data[ptr + 2]))
                ptr += 3

            answers.append(solve_case(n, v, a, b, queries))

        sys.stdout.write("\n".join(answers))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
