import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, k = data[0], data[1]
a = data[2:2 + n]

def grundy(x):
    if k % 2 == 0:
        if x == 1:
            return 1
        if x == 2:
            return 2
        return 1 if x % 2 == 0 else 0
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    if v == 0:
        return 1
    if v % 2 == 1:
        return 0
    return 2 if x == 1 else 1

xr = 0
for x in a:
    xr ^= grundy(x)

print("Kevin" if xr else "Nicky")
