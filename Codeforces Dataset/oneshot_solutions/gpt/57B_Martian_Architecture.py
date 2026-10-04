import sys
from bisect import bisect_left, bisect_right

data = list(map(int, sys.stdin.buffer.read().split()))
n, m, k = data[0], data[1], data[2]

roads_start = 3
query_start = roads_start + 3 * m

queries = sorted(data[query_start:query_start + k])

pref = [0]
for x in queries:
    pref.append(pref[-1] + x)

ans = 0

idx = roads_start
for _ in range(m):
    a = data[idx]
    b = data[idx + 1]
    c = data[idx + 2]
    idx += 3

    l = bisect_left(queries, a)
    r = bisect_right(queries, b)
    cnt = r - l
    if cnt:
        ans += cnt * (c - a) + (pref[r] - pref[l])

print(ans)
