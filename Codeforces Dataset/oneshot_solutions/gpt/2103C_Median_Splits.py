import sys

def possible(a, k):
    n = len(a)
    p = [0] * (n + 1)
    for i, x in enumerate(a, 1):
        p[i] = p[i - 1] + (1 if x <= k else -1)

    total = p[n]
    inf = 10 ** 9

    mn_nonneg = inf
    for r in range(2, n):
        v = p[r - 1]
        if v >= 0 and v < mn_nonneg:
            mn_nonneg = v
        if mn_nonneg <= p[r]:
            return True

    suff_min = [inf] * (n + 2)
    for i in range(n - 1, 0, -1):
        suff_min[i] = min(suff_min[i + 1], p[i])

    for l in range(1, n - 1):
        if p[l] >= 0 and suff_min[l + 1] <= total:
            return True

    mn = inf
    for r in range(2, n):
        if p[r - 1] < mn:
            mn = p[r - 1]
        if p[r] <= total and mn <= p[r]:
            return True

    return False

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n
        ans.append("YES" if possible(a, k) else "NO")

    print("\n".join(ans))

if __name__ == "__main__":
    main()
