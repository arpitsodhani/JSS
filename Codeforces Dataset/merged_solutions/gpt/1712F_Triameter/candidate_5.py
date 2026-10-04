# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import gc

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            n = data[0]
            pvals = data[1:n]
            qn = data[n]
            xs = data[n + 1:n + 1 + qn]

            parent = [-1] * n
            first = [-1] * n
            nxt = [-1] * n
            deg = [0] * n
            depth = [0] * n

            for i, p in enumerate(pvals, 1):
                p -= 1
                parent[i] = p
                nxt[i] = first[p]
                first[p] = i
                deg[i] += 1
                deg[p] += 1
                depth[i] = depth[p] + 1

            f = [-1] * n
            que = []
            for i, d in enumerate(deg):
                if d == 1:
                    f[i] = 0
                    que.append(i)

            head = 0
            while head < len(que):
                u = que[head]
                head += 1
                nd = f[u] + 1

                v = parent[u]
                if v != -1 and f[v] == -1:
                    f[v] = nd
                    que.append(v)

                c = first[u]
                while c != -1:
                    if f[c] == -1:
                        f[c] = nd
                        que.append(c)
                    c = nxt[c]

            neg = -10 ** 9

            def ok(limit, x):
                t = limit - x
                maps = [None] * n
                dep = depth
                ff = f
                fst = first
                nx = nxt

                for u in range(n - 1, -1, -1):
                    big = None
                    big_child = -1
                    c = fst[u]

                    while c != -1:
                        arr = maps[c]
                        if big is None or len(arr) > len(big):
                            big = arr
                            big_child = c
                        c = nx[c]

                    if big is None:
                        maps[u] = [dep[u]]
                        continue

                    base = dep[u] << 1
                    c = fst[u]
                    while c != -1:
                        if c != big_child:
                            small = maps[c]

                            for fv, dv in enumerate(small):
                                need = t - fv + 1
                                if need < 0:
                                    need = 0
                                if need < len(big) and dv + big[need] - base > limit:
                                    return False

                            for fv, dv in enumerate(small):
                                if dv > big[fv]:
                                    big[fv] = dv

                            maps[c] = None
                        c = nx[c]

                    need = t - ff[u] + 1
                    if need < 0:
                        need = 0
                    if need < len(big) and big[need] - dep[u] > limit:
                        return False

                    fu = ff[u]
                    if fu >= len(big):
                        big.extend([neg] * (fu + 1 - len(big)))
                    if dep[u] > big[fu]:
                        big[fu] = dep[u]

                    maps[u] = big

                return True

            gc.disable()

            order = sorted(range(qn), key=lambda i: xs[i])
            ans = [0] * qn
            last = 0

            for idx in order:
                x = xs[idx]
                lo, hi = last, n
                while lo < hi:
                    mid = (lo + hi) >> 1
                    if ok(mid, x):
                        hi = mid
                    else:
                        lo = mid + 1
                ans[idx] = lo
                last = lo

            print(*ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
