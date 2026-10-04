import sys

a = list(map(int, sys.stdin.read().split()))
n, k = a[0], a[1]
x = a[2:2 + n]

ans = 0
i = 0

while i < n - 1:
    j = i
    while j + 1 < n and x[j + 1] - x[i] <= k:
        j += 1
    if j == i:
        print(-1)
        sys.exit()
    ans += 1
    i = j

print(ans)
