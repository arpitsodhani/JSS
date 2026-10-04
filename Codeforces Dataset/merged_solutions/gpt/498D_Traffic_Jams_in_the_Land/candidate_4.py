# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    MOD = 60

    def compose(left, right):
        res = [0] * MOD
        for i in range(MOD):
            v = left[i]
            res[i] = v + right[(i + v) % MOD]
        return res

    def leaf(a):
        arr = [0] * MOD
        for i in range(MOD):
            arr[i] = 2 if i % a == 0 else 1
        return arr

    data = sys.stdin.buffer.read().split()
    if not data:
        sys.exit()

    p = 0
    n = int(data[p])
    p += 1

    a = [int(data[p + i]) for i in range(n)]
    p += n

    size = 1
    while size < n:
        size <<= 1

    identity = [0] * MOD
    seg = [identity[:] for _ in range(size << 1)]

    for i in range(n):
        seg[size + i] = leaf(a[i])

    for i in range(size - 1, 0, -1):
        seg[i] = compose(seg[i << 1], seg[i << 1 | 1])

    q = int(data[p])
    p += 1
    out = []

    for _ in range(q):
        typ = data[p]
        x = int(data[p + 1])
        y = int(data[p + 2])
        p += 3

        if typ == b'C':
            idx = size + x - 1
            seg[idx] = leaf(y)
            idx >>= 1
            while idx:
                seg[idx] = compose(seg[idx << 1], seg[idx << 1 | 1])
                idx >>= 1
        else:
            l = x - 1 + size
            r = y - 1 + size
            left_res = identity[:]
            right_res = identity[:]

            while l < r:
                if l & 1:
                    left_res = compose(left_res, seg[l])
                    l += 1
                if r & 1:
                    r -= 1
                    right_res = compose(seg[r], right_res)
                l >>= 1
                r >>= 1

            ans = compose(left_res, right_res)[0]
            out.append(str(ans))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
