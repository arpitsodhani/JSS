# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        from bisect import bisect_right
        from array import array

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            it = iter(data)

            n = next(it)
            m = next(it)

            edges = []
            weights = []
            for _ in range(m):
                v = next(it) - 1
                u = next(it) - 1
                w = next(it)
                edges.append((v, u, w))
                weights.append(w)

            p = next(it)
            k = next(it)
            a = next(it)
            b = next(it)
            c = next(it)

            queries = [next(it) for _ in range(p)]

            starts_set = {0}
            for w in weights:
                if w < c:
                    starts_set.add(w)

            for i in range(m):
                wi = weights[i]
                for j in range(i + 1, m):
                    s = (wi + weights[j]) // 2 + 1
                    if s < c:
                        starts_set.add(s)

            starts = sorted(starts_set)
            seg_count = len(starts)

            slopes = [0] * seg_count
            intercepts = [0] * seg_count
            base_order = list(range(m))

            for si, x in enumerate(starts):
                order = sorted(base_order, key=lambda idx: abs(weights[idx] - x))

                parent = list(range(n))
                size = [1] * n

                def find(v):
                    while parent[v] != v:
                        parent[v] = parent[parent[v]]
                        v = parent[v]
                    return v

                picked = 0
                slope = 0
                intercept = 0

                for ei in order:
                    v, u, w = edges[ei]
                    rv = find(v)
                    ru = find(u)

                    if rv != ru:
                        if size[rv] < size[ru]:
                            rv, ru = ru, rv
                        parent[ru] = rv
                        size[rv] += size[ru]

                        picked += 1
                        if w <= x:
                            slope += 1
                            intercept -= w
                        else:
                            slope -= 1
                            intercept += w

                        if picked == n - 1:
                            break

                slopes[si] = slope
                intercepts[si] = intercept

            shift = 7
            block = 1 << shift
            mask = block - 1
            block_count = (c + block - 1) // block

            table = [0] * block_count
            mixed = array('H')

            for bi in range(block_count):
                l = bi * block
                r = min(c, l + block)

                il = bisect_right(starts, l) - 1
                ir = bisect_right(starts, r - 1) - 1

                if il == ir:
                    table[bi] = il
                else:
                    off = len(mixed) // block
                    table[bi] = -off - 1

                    idx = il
                    nxt_i = idx + 1
                    nxt = starts[nxt_i] if nxt_i < seg_count else c

                    for x in range(l, l + block):
                        if x < r:
                            while x >= nxt:
                                idx += 1
                                nxt_i += 1
                                nxt = starts[nxt_i] if nxt_i < seg_count else c
                            mixed.append(idx)
                        else:
                            mixed.append(idx)

            ans = 0
            tab = table
            mix = mixed
            sl = slopes
            inter = intercepts

            for q in queries:
                idx = tab[q >> shift]
                if idx < 0:
                    idx = mix[((-idx - 1) << shift) + (q & mask)]
                ans ^= sl[idx] * q + inter[idx]

            q = queries[-1]
            for _ in range(k - p):
                q = (q * a + b) % c
                idx = tab[q >> shift]
                if idx < 0:
                    idx = mix[((-idx - 1) << shift) + (q & mask)]
                ans ^= sl[idx] * q + inter[idx]

            print(ans)

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
