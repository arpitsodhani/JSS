# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        sys.setrecursionlimit(1000000)

        R = 4000005

        seed = 123456789

        def rng():
            global seed
            seed ^= (seed << 13) & 0xffffffff
            seed ^= seed >> 17
            seed ^= (seed << 5) & 0xffffffff
            return seed

        class Node:
            __slots__ = ("l", "r", "p", "left", "right", "mx")
            def __init__(self, l, r):
                self.l = l
                self.r = r
                self.p = rng()
                self.left = None
                self.right = None
                self.mx = r - l + 1

        def val(t):
            return t.mx if t else 0

        def upd(t):
            if t:
                m = t.r - t.l + 1
                if t.left and t.left.mx > m:
                    m = t.left.mx
                if t.right and t.right.mx > m:
                    m = t.right.mx
                t.mx = m

        def merge(a, b):
            if not a or not b:
                return a or b
            if a.p > b.p:
                a.right = merge(a.right, b)
                upd(a)
                return a
            b.left = merge(a, b.left)
            upd(b)
            return b

        def split(t, key):
            if not t:
                return None, None
            if t.l < key:
                a, b = split(t.right, key)
                t.right = a
                upd(t)
                return t, b
            a, b = split(t.left, key)
            t.left = b
            upd(t)
            return a, t

        def add(root, node):
            a, b = split(root, node.l)
            return merge(merge(a, node), b)

        def erase(root, l):
            a, b = split(root, l)
            c, d = split(b, l + 1)
            return merge(a, d)

        def pred(root, x):
            res = None
            while root:
                if root.l <= x:
                    res = root
                    root = root.right
                else:
                    root = root.left
            return res

        def find_l(root, l):
            while root:
                if root.l == l:
                    return root
                if l < root.l:
                    root = root.left
                else:
                    root = root.right
            return None

        def first_with(root, k):
            while root:
                if val(root.left) >= k:
                    root = root.left
                elif root.r - root.l + 1 >= k:
                    return root.l
                else:
                    root = root.right
            return R + 1

        data = sys.stdin.buffer.read().split()
        it = 0
        t = int(data[it])
        it += 1
        out = []

        for _ in range(t):
            n = int(data[it])
            it += 1
            a = list(map(int, data[it:it + n]))
            it += n

            root = None
            cur = 1
            for x in a:
                if cur <= x - 1:
                    root = merge(root, Node(cur, x - 1))
                cur = x + 1
            if cur <= R:
                root = merge(root, Node(cur, R))

            m = int(data[it])
            it += 1
            ans = []

            for _ in range(m):
                op = data[it]
                x = int(data[it + 1])
                it += 2

                if op == b'?':
                    ans.append(str(first_with(root, x)))
                elif op == b'+':
                    q = pred(root, x)
                    l, r = q.l, q.r
                    root = erase(root, l)
                    if l <= x - 1:
                        root = add(root, Node(l, x - 1))
                    if x + 1 <= r:
                        root = add(root, Node(x + 1, r))
                else:
                    l = r = x
                    q = pred(root, x - 1)
                    if q and q.r == x - 1:
                        l = q.l
                        root = erase(root, q.l)
                    q = find_l(root, x + 1)
                    if q:
                        r = q.r
                        root = erase(root, q.l)
                    root = add(root, Node(l, r))

            out.append(" ".join(ans))

        sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
