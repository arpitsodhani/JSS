import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:]

counts = {}

for i in range(n):
    for j in range(i + 1, n):
        s = a[i] + a[j]
        counts[s] = counts.get(s, 0) + 1

print(max(counts.values()) if counts else 0)
