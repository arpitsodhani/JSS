import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2

        a = data[idx:idx + n - 1]
        idx += n - 1
        b = data[idx:idx + n]
        idx += n

        a.sort()
        b.sort()

        p = 0
        h = 0
        for x in b:
            if p < n - 1 and a[p] < x:
                h += 1
                p += 1

        need = h + 1

        def can(val):
            p = 0
            used = False
            cnt = 0

            for x in b:
                if used:
                    if p < n - 1 and a[p] < x:
                        cnt += 1
                        p += 1
                else:
                    if p < n - 1 and a[p] <= val:
                        cur = a[p]
                        from_a = True
                    else:
                        cur = val
                        from_a = False

                    if cur < x:
                        cnt += 1
                        if from_a:
                            p += 1
                        else:
                            used = True

                if cnt >= need:
                    return True

            return False

        if can(m):
            good = m
        elif not can(1):
            good = 0
        else:
            lo, hi = 1, m
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if can(mid):
                    lo = mid
                else:
                    hi = mid - 1
            good = lo

        out.append(str((n - h) * m - good))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
