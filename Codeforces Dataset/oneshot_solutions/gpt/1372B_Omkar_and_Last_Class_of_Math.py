import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
ans = []

for n in data[1:1 + t]:
    spf = n
    d = 2
    while d * d <= n:
        if n % d == 0:
            spf = d
            break
        d += 1
    a = n // spf
    ans.append(f"{a} {n - a}")

print("\n".join(ans))
