import sys

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
ans = []

for n in data[1:1 + t]:
    if n % 2:
        ans.append("-1")
    else:
        ans.append(f"0 0 {n // 2}")

sys.stdout.write("\n".join(ans))
