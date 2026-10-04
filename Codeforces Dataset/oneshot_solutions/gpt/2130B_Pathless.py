import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
p = 1
out = []

for _ in range(t):
    n = data[p]
    s = data[p + 1]
    p += 2
    a = data[p:p + n]
    p += n

    total = sum(a)
    if s < total:
        out.append(" ".join(map(str, a)))
    elif s == total:
        out.append("-1")
    elif s - total == 1:
        c0 = a.count(0)
        c1 = a.count(1)
        c2 = a.count(2)
        b = [0] * c0 + [2] * c2 + [1] * c1
        out.append(" ".join(map(str, b)))
    else:
        out.append("-1")

print("\n".join(out))
