import sys

n, m, k = map(int, sys.stdin.readline().split())

def side_sum(length, start):
    if start >= length:
        return length * (2 * start - length + 1) // 2
    return start * (start + 1) // 2 + (length - start)

def needed(x):
    return x + side_sum(k - 1, x - 1) + side_sum(n - k, x - 1)

lo, hi = 1, m
ans = 1

while lo <= hi:
    mid = (lo + hi) // 2
    if needed(mid) <= m:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
