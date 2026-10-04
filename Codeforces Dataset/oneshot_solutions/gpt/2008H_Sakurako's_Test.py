import sys

input = sys.stdin.readline

t = int(input())
out = []

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    pref = [0] * (n + 1)
    for v in a:
        pref[v] += 1
    for i in range(1, n + 1):
        pref[i] += pref[i - 1]

    need = n // 2 + 1
    ans = [0] * (n + 1)

    for x in range(1, n + 1):
        l, r = 0, x - 1
        while l < r:
            m = (l + r) // 2
            cnt = pref[m]
            k = x
            while k <= n:
                cnt += pref[min(k + m, n)] - pref[k - 1]
                k += x
            if cnt >= need:
                r = m
            else:
                l = m + 1
        ans[x] = l

    cur = []
    for _ in range(q):
        x = int(input())
        cur.append(str(ans[x]))
    out.append(" ".join(cur))

print("\n".join(out))
