import sys
from collections import Counter

data = sys.stdin.read().split()
n = int(data[0])
k = int(data[1])
s = data[2]

ans = 0
for cnt in sorted(Counter(s).values(), reverse=True):
    take = min(k, cnt)
    ans += take * take
    k -= take
    if k == 0:
        break

print(ans)
