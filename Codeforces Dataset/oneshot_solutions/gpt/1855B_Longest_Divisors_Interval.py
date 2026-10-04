import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []

for n in data[1:1 + t]:
    x = 1
    while n % x == 0:
        x += 1
    ans.append(str(x - 1))

print("\n".join(ans))
