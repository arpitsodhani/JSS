# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        p = 1
        out = []
        inf = 10 ** 9

        for _ in range(t):
            n = data[p]
            p += 1
            a = data[p:p + n]
            p += n

            zeros = []
            for i, x in enumerate(a, 1):
                if x == 0:
                    zeros.append(i)

            lft = [0] * (n + 1)
            rgt = [0] * (n + 1)

            mid = zeros[len(zeros) // 2] if zeros else 1

            c = 0
            for i in range(1, mid + 1):
                x = a[i - 1]
                if x == 0:
                    c += 1
                else:
                    lft[x] = c

            c = 0
            for i in range(n, mid, -1):
                x = a[i - 1]
                if x == 0:
                    c += 1
                else:
                    rgt[x] = c

            head = [-1] * (n + 1)
            nxt = [0] * (n + 1)
            left = [0] * (n + 1)
            freq = [0] * (n + 1)

            for x in range(1, n + 1):
                l = lft[x]
                r = rgt[x]
                left[x] = l
                freq[l] += 1
                nxt[x] = head[r]
                head[r] = x

            m = n + 1
            size = 1 << ((m - 1).bit_length())
            d = [-inf] * (size * 2)
            lazy = [0] * size

            pref = 0
            base = size
            for i in range(m):
                pref += freq[i]
                d[base + i] = -n - i + pref

            for i in range(size - 1, 0, -1):
                lv = d[i << 1]
                rv = d[i << 1 | 1]
                d[i] = lv if lv >= rv else rv

            lg = size.bit_length() - 1

            def apply(k, v):
                d[k] += v
                if k < size:
                    lazy[k] += v

            def pull(k):
                lv = d[k << 1]
                rv = d[k << 1 | 1]
                d[k] = (lv if lv >= rv else rv) + lazy[k]

            def add_suffix(l):
                ql = l + size
                qr = m + size
                l0 = ql
                r0 = qr
                while ql < qr:
                    if ql & 1:
                        apply(ql, -1)
                        ql += 1
                    if qr & 1:
                        qr -= 1
                        apply(qr, -1)
                    ql >>= 1
                    qr >>= 1
                for h in range(1, lg + 1):
                    pull(l0 >> h)
                    pull((r0 - 1) >> h)

            ans = len(zeros) // 2

            for r in range(n - 1, -1, -1):
                v = r - d[1]
                if v < ans:
                    ans = v
                e = head[r]
                while e != -1:
                    add_suffix(left[e])
                    e = nxt[e]

            out.append(str(ans))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
