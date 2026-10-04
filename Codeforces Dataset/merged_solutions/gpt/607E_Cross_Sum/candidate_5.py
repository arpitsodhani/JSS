# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import math

        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            sys.exit()

        n, p, q, m = data[:4]
        raw = data[4:]

        ks = []
        cs = []
        rhos = []
        thetas = []

        twopi = 2.0 * math.pi

        for i in range(n):
            a = raw[2 * i]
            b = raw[2 * i + 1]
            k = a / 1000.0
            c = (a * p + 1000 * b - 1000 * q) / 1000000.0
            s = math.hypot(k, 1.0)
            rho = c / s
            theta = math.atan2(1.0, -k)
            if rho < 0:
                rho = -rho
                theta += math.pi
            theta %= twopi
            ks.append(k)
            cs.append(c)
            rhos.append(rho)
            thetas.append(theta)

        class BIT:
            __slots__ = ("n", "bit")
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)

            def add(self, i, v):
                i += 1
                n = self.n
                bit = self.bit
                while i <= n:
                    bit[i] += v
                    i += i & -i

            def sum(self, i):
                i += 1
                bit = self.bit
                s = 0
                while i > 0:
                    s += bit[i]
                    i -= i & -i
                return s

            def kth(self, k):
                idx = 0
                bitmask = 1 << (self.n.bit_length() - 1)
                bit = self.bit
                while bitmask:
                    nxt = idx + bitmask
                    if nxt <= self.n and bit[nxt] < k:
                        idx = nxt
                        k -= bit[nxt]
                    bitmask >>= 1
                return idx

        def events_for_radius(r):
            ev = []
            invr = 1.0 / r
            for i in range(n):
                rho = rhos[i]
                if rho <= r:
                    d = math.acos(max(-1.0, min(1.0, rho * invr)))
                    a = (thetas[i] - d) % twopi
                    b = (thetas[i] + d) % twopi
                    if a > b:
                        a, b = b, a
                    ev.append((a, i))
                    ev.append((b, i))
            ev.sort()
            return ev

        def count_inside(r, cap):
            if r <= 0.0:
                return 0
            ev = events_for_radius(r)
            bit = BIT(len(ev) + 2)
            first = [-1] * n
            active = 0
            ans = 0
            for pos, (_, idx) in enumerate(ev):
                f = first[idx]
                if f < 0:
                    first[idx] = pos
                    bit.add(pos, 1)
                    active += 1
                else:
                    ans += active - bit.sum(f)
                    if ans >= cap:
                        return ans
                    bit.add(f, -1)
                    active -= 1
            return ans

        def dist_pair(i, j):
            dk = ks[i] - ks[j]
            if abs(dk) < 1e-18:
                return None
            x = (cs[j] - cs[i]) / dk
            y = ks[i] * x + cs[i]
            return math.hypot(x, y)

        def sum_strict(r):
            if r <= 0.0:
                return 0, 0.0
            ev = events_for_radius(r)
            size = len(ev) + 2
            bit = BIT(size)
            first = [-1] * n
            at = [-1] * size
            active = 0
            cnt = 0
            total = 0.0
            for pos, (_, idx) in enumerate(ev):
                f = first[idx]
                if f < 0:
                    first[idx] = pos
                    at[pos] = idx
                    bit.add(pos, 1)
                    active += 1
                else:
                    before = bit.sum(f)
                    have = active - before
                    target = before + 1
                    for _ in range(have):
                        ppos = bit.kth(target)
                        j = at[ppos]
                        d = dist_pair(idx, j)
                        if d is not None and d < r:
                            cnt += 1
                            total += d
                        target += 1
                    bit.add(f, -1)
                    active -= 1
            return cnt, total

        total_pairs = n * (n - 1) // 2

        if total_pairs <= 2000000:
            arr = []
            for i in range(n):
                ki = ks[i]
                ci = cs[i]
                for j in range(i + 1, n):
                    dk = ki - ks[j]
                    if abs(dk) > 1e-18:
                        x = (cs[j] - ci) / dk
                        y = ki * x + ci
                        arr.append(math.hypot(x, y))
            arr.sort()
            print("{:.9f}".format(sum(arr[:m])))
        else:
            hi = 1.0
            while count_inside(hi, m) < m:
                hi *= 2.0
            lo = 0.0
            for _ in range(60):
                mid = (lo + hi) * 0.5
                if count_inside(mid, m) >= m:
                    hi = mid
                else:
                    lo = mid
            t = hi
            r = max(0.0, t - 1e-7)
            cnt, total = sum_strict(r)
            ans = total + (m - cnt) * t
            print("{:.9f}".format(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
