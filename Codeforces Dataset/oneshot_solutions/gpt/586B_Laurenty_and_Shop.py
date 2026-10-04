import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a1 = data[1:n]
a2 = data[n:2 * n - 1]
b = data[2 * n - 1:3 * n - 1]

top_total = sum(a1)
bottom_total = sum(a2)

best = 10**18
pref_top = 0
pref_bottom = 0

for i in range(n):
    if i > 0:
        pref_top += a1[i - 1]
        pref_bottom += a2[i - 1]
    cost = top_total + bottom_total + b[i] + min(pref_top, pref_bottom) + min(top_total - pref_top, bottom_total - pref_bottom)
    best = min(best, cost)

print(best)
