# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys
        import math

        def fft(a, invert):
            n = len(a)
            j = 0
            for i in range(1, n):
                bit = n >> 1
                while j & bit:
                    j ^= bit
                    bit >>= 1
                j ^= bit
                if i < j:
                    a[i], a[j] = a[j], a[i]

            length = 2
            while length <= n:
                ang = 2.0 * math.pi / length
                if invert:
                    ang = -ang
                wlen = complex(math.cos(ang), math.sin(ang))
                half = length >> 1
                for i in range(0, n, length):
                    w = 1 + 0j
                    end = i + half
                    for j in range(i, end):
                        u = a[j]
                        v = a[j + half] * w
                        a[j] = u + v
                        a[j + half] = u - v
                        w *= wlen
                length <<= 1

            if invert:
                inv_n = 1.0 / n
                for i in range(n):
                    a[i] *= inv_n

        def convolution(a, b):
            need = len(a) + len(b) - 1
            n = 1
            while n < need:
                n <<= 1
            fa = [0j] * n
            for i, x in enumerate(a):
                fa[i] = complex(x, b[i] if i < len(b) else 0)
            fft(fa, False)
            fa0 = fa[0]
            fa[0] = complex(fa0.real * fa0.imag * 2, 0)
            for i in range(1, n):
                j = n - i
                x = fa[i]
                y = fa[j].conjugate()
                p = (x + y) * 0.5
                q = (x - y) * (-0.5j)
                fa[i] = p * q * 2
            fft(fa, True)
            return [int(fa[i].real + 0.5) for i in range(need)]

        def dist(mask):
            parent = list(range(6))

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            edges = 0
            for i in range(6):
                for j in range(i + 1, 6):
                    if mask & (1 << edges):
                        ri = find(i)
                        rj = find(j)
                        if ri != rj:
                            parent[ri] = rj
                    edges += 1

            seen = [0] * 6
            ans = 0
            for i in range(6):
                r = find(i)
                seen[r] += 1
            for x in seen:
                if x:
                    ans += x - 1
            return ans

        def main():
            data = sys.stdin.read().split()
            if len(data) < 2:
                return
            s, t = data[0], data[1]
            n, m = len(s), len(t)
            k = n - m + 1

            edge_id = [[-1] * 6 for _ in range(6)]
            e = 0
            for i in range(6):
                for j in range(i + 1, 6):
                    edge_id[i][j] = edge_id[j][i] = e
                    e += 1

            masks = [0] * k
            rs = [[0] * n for _ in range(6)]
            rt = [[0] * m for _ in range(6)]

            for i, ch in enumerate(s):
                rs[ord(ch) - 97][i] = 1
            for i, ch in enumerate(reversed(t)):
                rt[ord(ch) - 97][i] = 1

            for a in range(6):
                for b in range(a + 1, 6):
                    c1 = convolution(rs[a], rt[b])
                    c2 = convolution(rs[b], rt[a])
                    bit = 1 << edge_id[a][b]
                    base = m - 1
                    for i in range(k):
                        if c1[base + i] or c2[base + i]:
                            masks[i] |= bit

            val = [dist(i) for i in range(1 << 15)]
            print(" ".join(str(val[x]) for x in masks))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
