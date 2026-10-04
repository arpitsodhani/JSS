# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    n = data[p]
    m = data[p + 1]
    p += 2
    a = [0] + data[p:p + n]
    p += n
    b = [0] + data[p:p + n]
    p += n

    size = 4 * n + 8
    stamp = [0] * size
    shift = [0] * size

    def put(v, l, r, ql, qr, delta, t):
        if ql <= l and r <= qr:
            stamp[v] = t
            shift[v] = delta
            return
        mid = (l + r) >> 1
        if ql <= mid:
            put(v << 1, l, mid, ql, qr, delta, t)
        if mid < qr:
            put(v << 1 | 1, mid + 1, r, ql, qr, delta, t)

    def get(pos):
        v = 1
        l = 1
        r = n
        best = 0
        delta = 0
        while True:
            if stamp[v] > best:
                best = stamp[v]
                delta = shift[v]
            if l == r:
                break
            mid = (l + r) >> 1
            if pos <= mid:
                v <<= 1
                r = mid
            else:
                v = v << 1 | 1
                l = mid + 1
        if best:
            return a[pos + delta]
        return b[pos]

    out = []
    for t in range(1, m + 1):
        typ = data[p]
        p += 1
        if typ == 1:
            x = data[p]
            y = data[p + 1]
            k = data[p + 2]
            p += 3
            put(1, 1, n, y, y + k - 1, x - y, t)
        else:
            pos = data[p]
            p += 1
            out.append(str(get(pos)))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
