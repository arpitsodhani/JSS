# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = (data[0], data[1])
    a = data[2:2 + n]
    pos = 2 + n
    queries = []
    for idx in range(m):
        l = data[pos]
        r = data[pos + 1]
        pos += 2
        queries.append((r, l, idx))
    queries.sort()
    inf = 10 ** 18
    size = 1
    while size < n:
        size <<= 1
    seg = [inf] * (2 * size)

    def update(i, val):
        i += size - 1
        if val >= seg[i]:
            return
        seg[i] = val
        i >>= 1
        while i:
            nv = seg[i << 1] if seg[i << 1] < seg[i << 1 | 1] else seg[i << 1 | 1]
            if seg[i] == nv:
                break
            seg[i] = nv
            i >>= 1

    def query(l, r):
        l += size - 1
        r += size - 1
        res = inf
        while l <= r:
            if l & 1:
                if seg[l] < res:
                    res = seg[l]
                l += 1
            if not r & 1:
                if seg[r] < res:
                    res = seg[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res
    last = {}
    ans = [-1] * m
    qi = 0
    for i, x in enumerate(a, 1):
        if x in last:
            p = last[x]
            update(p, i - p)
        last[x] = i
        while qi < m and queries[qi][0] == i:
            _, l, idx = queries[qi]
            res = query(l, i)
            ans[idx] = -1 if res == inf else res
            qi += 1
    sys.stdout.write('\n'.join(map(str, ans)))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
