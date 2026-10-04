import sys

data = list(map(int, sys.stdin.read().split()))
n, k = data[0], data[1]
a = data[2:2 + n]

pref = [0]
for x in a:
    pref.append(pref[-1] + x)

ans = 0.0
for length in range(k, n + 1):
    for l in range(0, n - length + 1):
        s = pref[l + length] - pref[l]
        ans = max(ans, s / length)

print(ans)
