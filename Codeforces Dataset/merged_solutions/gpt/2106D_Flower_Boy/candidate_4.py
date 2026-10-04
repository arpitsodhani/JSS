# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        t = data[0]
        idx = 1
        out = []

        INF = 10**30

        for _ in range(t):
            n = data[idx]
            m = data[idx + 1]
            idx += 2

            a = data[idx:idx + n]
            idx += n

            b = data[idx:idx + m]
            idx += m

            pref = [0] * (n + 1)
            j = 0
            for i, x in enumerate(a):
                if j < m and x >= b[j]:
                    j += 1
                pref[i + 1] = j

            if pref[n] == m:
                out.append("0")
                continue

            suff = [0] * (n + 1)
            j = m - 1
            cnt = 0
            for i in range(n - 1, -1, -1):
                if j >= 0 and a[i] >= b[j]:
                    j -= 1
                    cnt += 1
                suff[i] = cnt

            size = 1
            while size < m:
                size <<= 1

            seg = [INF] * (2 * size)
            for i, x in enumerate(b):
                seg[size + i] = x
            for i in range(size - 1, 0, -1):
                seg[i] = min(seg[i << 1], seg[i << 1 | 1])

            def range_min(l, r):
                l += size
                r += size
                res = INF
                while l <= r:
                    if l & 1:
                        res = min(res, seg[l])
                        l += 1
                    if not (r & 1):
                        res = min(res, seg[r])
                        r -= 1
                    l >>= 1
                    r >>= 1
                return res

            ans = INF
            for split in range(n + 1):
                left = pref[split]
                right = suff[split]

                lo = m - right
                hi = left + 1

                if lo <= hi:
                    lo = max(lo, 1)
                    hi = min(hi, m)
                    if lo <= hi:
                        ans = min(ans, range_min(lo - 1, hi - 1))

            out.append(str(ans if ans < INF else -1))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
