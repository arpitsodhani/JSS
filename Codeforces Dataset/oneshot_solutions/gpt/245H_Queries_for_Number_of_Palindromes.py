import sys
from array import array

data = sys.stdin.buffer.read().split()
s = data[0].decode()
n = len(s)

pal = [bytearray(n) for _ in range(n)]
dp = [array('I', [0]) * n for _ in range(n)]

for length in range(1, n + 1):
    end = n - length + 1
    if length == 1:
        for i in range(n):
            pal[i][i] = 1
            dp[i][i] = 1
    else:
        inner_short = length <= 2
        for l in range(end):
            r = l + length - 1
            p = 1 if s[l] == s[r] and (inner_short or pal[l + 1][r - 1]) else 0
            pal[l][r] = p
            dp[l][r] = dp[l + 1][r] + dp[l][r - 1] - dp[l + 1][r - 1] + p

q = int(data[1])
out = []
idx = 2
for _ in range(q):
    l = int(data[idx]) - 1
    r = int(data[idx + 1]) - 1
    idx += 2
    out.append(str(dp[l][r]))

sys.stdout.write("\n".join(out))
