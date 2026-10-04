import sys

data = sys.stdin.read().split()
n = int(data[0])
p = list(map(int, data[1:1 + n]))
s = data[1 + n].strip()

base = 0
best = 0

cur = 0
for x, c in zip(p, s):
    if c == 'B':
        base += x
        cur -= x
    else:
        cur += x
    if cur > best:
        best = cur

cur = 0
for x, c in zip(reversed(p), reversed(s)):
    if c == 'B':
        cur -= x
    else:
        cur += x
    if cur > best:
        best = cur

print(base + best)
