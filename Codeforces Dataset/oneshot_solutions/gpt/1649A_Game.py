import sys

data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    idx += 1
    a = data[idx:idx + n]
    idx += n

    zeros = [i for i, v in enumerate(a) if v == 0]
    if not zeros:
        ans.append("0")
    else:
        ans.append(str(zeros[-1] - zeros[0] + 2))

print("\n".join(ans))
