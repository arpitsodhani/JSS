import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)

    a = [0] + [next(it) for _ in range(n)]
    b = [0] + [next(it) for _ in range(n)]

    lazy_time = [0] * (4 * n + 5)
    lazy_shift = [0] * (4 * n + 5)

    def update(node, left, right, ql, qr, shift, tm):
        if ql <= left and right <= qr:
            lazy_time[node] = tm
            lazy_shift[node] = shift
            return
        mid = (left + right) // 2
        if ql <= mid:
            update(node * 2, left, mid, ql, qr, shift, tm)
        if mid < qr:
            update(node * 2 + 1, mid + 1, right, ql, qr, shift, tm)

    def query(node, left, right, pos):
        best_time = lazy_time[node]
        best_shift = lazy_shift[node]

        while left != right:
            mid = (left + right) // 2
            if pos <= mid:
                node = node * 2
                right = mid
            else:
                node = node * 2 + 1
                left = mid + 1

            if lazy_time[node] > best_time:
                best_time = lazy_time[node]
                best_shift = lazy_shift[node]

        if best_time == 0:
            return b[pos]
        return a[pos + best_shift]

    out = []
    tm = 0

    for _ in range(m):
        typ = next(it)
        if typ == 1:
            x = next(it)
            y = next(it)
            k = next(it)
            tm += 1
            update(1, 1, n, y, y + k - 1, x - y, tm)
        else:
            x = next(it)
            out.append(str(query(1, 1, n, x)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
