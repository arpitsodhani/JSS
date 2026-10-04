import sys

def can_make(k, c):
    if k == 0:
        return True
    total = sum(c)
    if total < 4 * k:
        return False

    for a in range(k + 1):
        need0 = k - a
        need1 = a
        if c[0] < need0 or c[1] < need1:
            continue

        rem = c[:]
        rem[0] -= need0
        rem[1] -= need1

        bmax = min(a, rem[0] + rem[1])
        for b in range(bmax + 1):
            r = rem[:]
            take0 = min(r[0], b)
            r[0] -= take0
            left = b - take0
            if r[1] < left:
                continue
            r[1] -= left

            free_hour = k - a
            if sum(r) < free_hour + 2 * k:
                continue

            use_free = free_hour
            for d in range(10):
                t = min(r[d], use_free)
                r[d] -= t
                use_free -= t
                if use_free == 0:
                    break
            if use_free:
                continue

            if sum(r[:6]) >= k:
                return True

    return False

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    ans = []

    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2

        c = [0] * 10
        for ch in s:
            c[ord(ch) - 48] += 1

        lo, hi = 0, n // 4
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_make(mid, c):
                lo = mid
            else:
                hi = mid - 1
        ans.append(str(lo))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
