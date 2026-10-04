import sys

data = list(map(int, sys.stdin.read().split()))
n, k = data[0], data[1]
a = data[2:2 + n]

ans = sum(x // 10 for x in a)

need = []
for x in a:
    if x < 100 and x % 10 != 0:
        need.append(10 - x % 10)

need.sort()

for c in need:
    if k >= c:
        k -= c
        ans += 1
    else:
        break

for x in a:
    add = min(k, 100 - x)
    gain = add // 10
    ans += gain
    k -= gain * 10

print(ans)
