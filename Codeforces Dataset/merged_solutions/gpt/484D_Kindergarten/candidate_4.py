# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    class SegTree:
        def __init__(self, n):
            self.n = n
            size = 4 * n + 5
            self.mx = [-(10**30)] * size
            self.lazy = [0] * size

        def _apply(self, v, add):
            self.mx[v] += add
            self.lazy[v] += add

        def _push(self, v):
            z = self.lazy[v]
            if z:
                self._apply(v * 2, z)
                self._apply(v * 2 + 1, z)
                self.lazy[v] = 0

        def add(self, v, l, r, ql, qr, val):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                self._apply(v, val)
                return
            self._push(v)
            m = (l + r) // 2
            self.add(v * 2, l, m, ql, qr, val)
            self.add(v * 2 + 1, m + 1, r, ql, qr, val)
            self.mx[v] = self.mx[v * 2] if self.mx[v * 2] > self.mx[v * 2 + 1] else self.mx[v * 2 + 1]

        def setpos(self, v, l, r, pos, val):
            if l == r:
                self.mx[v] = val
                self.lazy[v] = 0
                return
            self._push(v)
            m = (l + r) // 2
            if pos <= m:
                self.setpos(v * 2, l, m, pos, val)
            else:
                self.setpos(v * 2 + 1, m + 1, r, pos, val)
            self.mx[v] = self.mx[v * 2] if self.mx[v * 2] > self.mx[v * 2 + 1] else self.mx[v * 2 + 1]

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return
        n = data[0]
        a = data[1:1 + n]

        seg = SegTree(n)
        max_stack = []
        min_stack = []
        dp_prev = 0

        for i, x in enumerate(a, 1):
            seg.setpos(1, 1, n, i, dp_prev)

            left = i
            while max_stack and max_stack[-1][0] <= x:
                val, l = max_stack.pop()
                seg.add(1, 1, n, l, left - 1, x - val)
                left = l
            max_stack.append((x, left))

            left = i
            while min_stack and min_stack[-1][0] >= x:
                val, l = min_stack.pop()
                seg.add(1, 1, n, l, left - 1, val - x)
                left = l
            min_stack.append((x, left))

            dp_prev = seg.mx[1]

        print(dp_prev)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
