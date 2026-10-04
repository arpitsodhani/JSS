# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        MOD = 10 ** 9 + 7

        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            sys.exit()

        k, n, m = data[0], data[1], data[2]
        p = 3

        events = [[] for _ in range(k + 1)]
        for _ in range(n):
            l, r = data[p], data[p + 1]
            p += 2
            events[r].append((l, 0))

        for _ in range(m):
            l, r = data[p], data[p + 1]
            p += 2
            events[r].append((l, 1))

        size = 1
        while size < k + 2:
            size <<= 1

        tree0 = [0] * (size * 2)
        tree1 = [0] * (size * 2)
        lazy0 = [None] * (size * 2)
        lazy1 = [None] * (size * 2)

        def apply(tree, lazy, idx, value):
            tree[idx] = value
            lazy[idx] = value

        def push(tree, lazy, idx):
            value = lazy[idx]
            if value is not None:
                apply(tree, lazy, idx * 2, value)
                apply(tree, lazy, idx * 2 + 1, value)
                lazy[idx] = None

        def point_set(tree, lazy, pos, value, idx=1, left=0, right=None):
            if right is None:
                right = size - 1
            if left == right:
                tree[idx] = value
                lazy[idx] = None
                return
            push(tree, lazy, idx)
            mid = (left + right) >> 1
            if pos <= mid:
                point_set(tree, lazy, pos, value, idx * 2, left, mid)
            else:
                point_set(tree, lazy, pos, value, idx * 2 + 1, mid + 1, right)
            tree[idx] = (tree[idx * 2] + tree[idx * 2 + 1]) % MOD

        def range_set(tree, lazy, ql, qr, value, idx=1, left=0, right=None):
            if right is None:
                right = size - 1
            if ql > right or qr < left:
                return
            if ql <= left and right <= qr:
                apply(tree, lazy, idx, value)
                return
            push(tree, lazy, idx)
            mid = (left + right) >> 1
            range_set(tree, lazy, ql, qr, value, idx * 2, left, mid)
            range_set(tree, lazy, ql, qr, value, idx * 2 + 1, mid + 1, right)
            tree[idx] = (tree[idx * 2] + tree[idx * 2 + 1]) % MOD

        def range_sum(tree, lazy, ql, qr, idx=1, left=0, right=None):
            if right is None:
                right = size - 1
            if ql > right or qr < left:
                return 0
            if ql <= left and right <= qr:
                return tree[idx]
            push(tree, lazy, idx)
            mid = (left + right) >> 1
            return (range_sum(tree, lazy, ql, qr, idx * 2, left, mid) +
                    range_sum(tree, lazy, ql, qr, idx * 2 + 1, mid + 1, right)) % MOD

        point_set(tree0, lazy0, 0, 1)
        point_set(tree1, lazy1, 0, 1)

        for i in range(1, k + 1):
            total0 = tree0[1]
            total1 = tree1[1]
            point_set(tree0, lazy0, i, total1)
            point_set(tree1, lazy1, i, total0)

            for l, typ in events[i]:
                if typ == 0:
                    s = range_sum(tree1, lazy1, l, i)
                    range_set(tree1, lazy1, l, i, 0)
                    point_set(tree1, lazy1, l - 1, (range_sum(tree1, lazy1, l - 1, l - 1) + s) % MOD)
                else:
                    s = range_sum(tree0, lazy0, l, i)
                    range_set(tree0, lazy0, l, i, 0)
                    point_set(tree0, lazy0, l - 1, (range_sum(tree0, lazy0, l - 1, l - 1) + s) % MOD)

        print((tree0[1] + tree1[1]) % MOD)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
