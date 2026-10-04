# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def process(a, l, r, val):
        v = []
        curr = 0
        for x in range(l, r + 1):
            res0 = x
            res1 = 0
            ax = a[x]
            while v and a[v[-1][0]] < ax:
                t = v[-1][1]
                v.pop()
                if v and v[-1][1] < t + 1:
                    v[-1][1] = t + 1
                if res1 < t + 1:
                    res1 = t + 1
            v.append([res0, res1])
            cur = res1 + len(v)
            if curr < cur:
                curr = cur
            val[x] = curr
        return v

    def solve_case(n, p):
        a = [0] + p[:]
        ans = [[0] * (n + 2), [0] * (n + 2)]
        t = [0] * (n + 2)
        stks = []

        for z in range(2):
            v = process(a, 1, n, ans[z])
            stks.append([x[0] for x in v])
            a[1:] = reversed(a[1:])

        root = stks[0][0]
        mx = ans[0][root] + ans[1][n - root + 1] - 1

        for z in range(2):
            stk = stks[z]
            for i in range(len(stk) - 1):
                l = stk[i]
                r = stk[i + 1]
                process(a, l, r, t)
                other = ans[z ^ 1]
                for y in range(l, r):
                    val = t[y] + other[n - y]
                    if mx < val:
                        mx = val
            a[1:] = reversed(a[1:])

        return mx - 1

    def main():
        data = sys.stdin.buffer.read().split()
        it = iter(data)
        tc = int(next(it))
        out = []
        for _ in range(tc):
            n = int(next(it))
            p = [int(next(it)) for _ in range(n)]
            next(it)
            out.append(str(solve_case(n, p)))
        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
