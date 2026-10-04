# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from bisect import bisect_left, bisect_right

        INF = 10 ** 30

        class Block:
            __slots__ = ("l", "r", "m", "all", "vals", "vkeys", "vmasks", "mnkeys", "mnmasks",
                         "mxkeys", "mxmasks", "mn_lt_a", "mx_gt_a", "bmn", "bmx")

            def __init__(self, a, l, r):
                self.l = l
                self.r = r
                self.m = r - l
                self.all = (1 << self.m) - 1
                self.vals = a[l:r]
                self.bmn = min(self.vals)
                self.bmx = max(self.vals)

                smin = [INF] * self.m
                smax = [-INF] * self.m
                mn = INF
                mx = -INF
                for i in range(self.m - 1, -1, -1):
                    smin[i] = mn
                    smax[i] = mx
                    v = self.vals[i]
                    if v < mn:
                        mn = v
                    if v > mx:
                        mx = v

                self.mn_lt_a = 0
                self.mx_gt_a = 0
                for i, v in enumerate(self.vals):
                    bit = 1 << i
                    if smin[i] < v:
                        self.mn_lt_a |= bit
                    if smax[i] > v:
                        self.mx_gt_a |= bit

                self.vkeys, self.vmasks = self._build_masks(self.vals)
                self.mnkeys, self.mnmasks = self._build_masks(smin)
                self.mxkeys, self.mxmasks = self._build_masks(smax)

            def _build_masks(self, arr):
                pairs = sorted((v, i) for i, v in enumerate(arr))
                keys = []
                masks = []
                mask = 0
                p = 0
                n = len(pairs)
                while p < n:
                    v = pairs[p][0]
                    while p < n and pairs[p][0] == v:
                        mask |= 1 << pairs[p][1]
                        p += 1
                    keys.append(v)
                    masks.append(mask)
                return keys, masks

            def _le(self, keys, masks, x):
                p = bisect_right(keys, x) - 1
                return masks[p] if p >= 0 else 0

            def _lt(self, keys, masks, x):
                p = bisect_left(keys, x) - 1
                return masks[p] if p >= 0 else 0

            def val_le(self, x):
                return self._le(self.vkeys, self.vmasks, x)

            def val_lt(self, x):
                return self._lt(self.vkeys, self.vmasks, x)

            def val_gt(self, x):
                return self.all ^ self._le(self.vkeys, self.vmasks, x)

            def val_ge(self, x):
                return self.all ^ self._lt(self.vkeys, self.vmasks, x)

            def mn_lt(self, x):
                return self._lt(self.mnkeys, self.mnmasks, x)

            def mx_gt(self, x):
                return self.all ^ self._le(self.mxkeys, self.mxmasks, x)

            def query3(self, x, emn, emx):
                le = self.val_le(x)
                ge = self.val_ge(x)

                c1 = self.mn_lt_a | self.val_gt(emn)
                c2 = self.all if emx > x else self.mx_gt(x)
                r1 = le & (c1 | c2)

                c3 = self.all if emn < x else self.mn_lt(x)
                c4 = self.mx_gt_a | self.val_lt(emx)
                r2 = ge & (c3 | c4)

                res = r1 | r2
                if res:
                    return self.l + res.bit_length() - 1
                return -1

            def query4(self, x, emn, emx):
                le = self.val_le(x)
                ge = self.val_ge(x)

                c1 = self.mn_lt_a | self.val_gt(emn)
                c2 = self.all if emx > x else self.mx_gt(x)
                r1 = le & c1 & c2

                c3 = self.all if emn < x else self.mn_lt(x)
                c4 = self.mx_gt_a | self.val_lt(emx)
                r2 = ge & c3 & c4

                res = r1 | r2
                if res:
                    return self.l + res.bit_length() - 1
                return -1


        class RangeAssignPointQuery:
            def __init__(self, n):
                self.n = n
                self.t = [None] * (4 * n + 5)

            def update(self, ql, qr, val, node=1, l=0, r=None):
                if r is None:
                    r = self.n - 1
                if ql > r or qr < l:
                    return
                if ql <= l and r <= qr:
                    self.t[node] = val
                    return
                m = (l + r) >> 1
                self.update(ql, qr, val, node << 1, l, m)
                self.update(ql, qr, val, node << 1 | 1, m + 1, r)

            def get(self, pos):
                node = 1
                l = 0
                r = self.n - 1
                ans = None
                while True:
                    if self.t[node] is not None:
                        ans = self.t[node]
                    if l == r:
                        return ans
                    m = (l + r) >> 1
                    if pos <= m:
                        node <<= 1
                        r = m
                    else:
                        node = node << 1 | 1
                        l = m + 1


        def build_sparse(a):
            n = len(a)
            lg = [0] * (n + 1)
            for i in range(2, n + 1):
                lg[i] = lg[i >> 1] + 1
            stmn = [list(range(n))]
            stmx = [list(range(n))]
            k = 1
            while (1 << k) <= n:
                prevmn = stmn[-1]
                prevmx = stmx[-1]
                step = 1 << (k - 1)
                size = n - (1 << k) + 1
                cmn = [0] * size
                cmx = [0] * size
                for i in range(size):
                    x = prevmn[i]
                    y = prevmn[i + step]
                    cmn[i] = x if a[x] <= a[y] else y
                    x = prevmx[i]
                    y = prevmx[i + step]
                    cmx[i] = x if a[x] >= a[y] else y
                stmn.append(cmn)
                stmx.append(cmx)
                k += 1
            return lg, stmn, stmx

        def rmq_idx(a, lg, st, l, r, is_min):
            k = lg[r - l + 1]
            x = st[k][l]
            y = st[k][r - (1 << k) + 1]
            if is_min:
                return x if a[x] <= a[y] else y
            return x if a[x] >= a[y] else y

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return
            n, q = data[0], data[1]
            a = data[2:2 + n]
            raw = data[2 + n:]
            queries = []
            by_r = [[] for _ in range(n)]
            for qi in range(q):
                l = raw[2 * qi] - 1
                r = raw[2 * qi + 1] - 1
                queries.append((l, r))
                by_r[r].append((l, qi))

            lg, stmn, stmx = build_sparse(a)

            B = 700
            blocks = []
            bid = [0] * n
            for l in range(0, n, B):
                r = min(n, l + B)
                b = Block(a, l, r)
                idx = len(blocks)
                blocks.append(b)
                for i in range(l, r):
                    bid[i] = idx

            seg3 = RangeAssignPointQuery(n)
            seg4 = RangeAssignPointQuery(n)
            ans = [None] * q

            for r in range(n):
                best3 = -1
                best4 = -1

                if r >= 2:
                    b = bid[r - 1]
                    bl = blocks[b].l
                    mn = INF
                    mx = -INF
                    for i in range(r - 2, bl - 1, -1):
                        v = a[i + 1]
                        if v < mn:
                            mn = v
                        if v > mx:
                            mx = v
                        lo = a[i] if a[i] < a[r] else a[r]
                        hi = a[i] if a[i] > a[r] else a[r]
                        if best3 < 0 and (mn < lo or mx > hi):
                            best3 = i
                        if best4 < 0 and mn < lo and mx > hi:
                            best4 = i
                        if best3 >= 0 and best4 >= 0:
                            break

                    emn = min(a[bl:r])
                    emx = max(a[bl:r])
                    bb = b - 1
                    while bb >= 0 and (best3 < 0 or best4 < 0):
                        block = blocks[bb]
                        if best3 < 0:
                            x = block.query3(a[r], emn, emx)
                            if x >= 0:
                                best3 = x
                        if best4 < 0:
                            x = block.query4(a[r], emn, emx)
                            if x >= 0:
                                best4 = x
                        if block.bmn < emn:
                            emn = block.bmn
                        if block.bmx > emx:
                            emx = block.bmx
                        bb -= 1

                if best3 >= 0:
                    i = best3
                    lo = a[i] if a[i] < a[r] else a[r]
                    hi = a[i] if a[i] > a[r] else a[r]
                    mnpos = rmq_idx(a, lg, stmn, i + 1, r - 1, True)
                    if a[mnpos] < lo:
                        tup = (i, mnpos, r)
                    else:
                        mxpos = rmq_idx(a, lg, stmx, i + 1, r - 1, False)
                        tup = (i, mxpos, r)
                    seg3.update(0, i, tup)

                if best4 >= 0:
                    i = best4
                    mnpos = rmq_idx(a, lg, stmn, i + 1, r - 1, True)
                    mxpos = rmq_idx(a, lg, stmx, i + 1, r - 1, False)
                    if mnpos < mxpos:
                        tup = (i, mnpos, mxpos, r)
                    else:
                        tup = (i, mxpos, mnpos, r)
                    seg4.update(0, i, tup)

                for l, qi in by_r[r]:
                    t = seg4.get(l)
                    if t is not None:
                        ans[qi] = t
                    else:
                        ans[qi] = seg3.get(l)

            out = []
            for t in ans:
                if t is None:
                    out.append("0")
                else:
                    out.append(str(len(t)))
                    out.append(" ".join(str(x + 1) for x in t) + " ")
            sys.stdout.write("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
