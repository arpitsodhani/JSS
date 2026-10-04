import sys
input = sys.stdin.readline

def can_complete(segments, k):
    left, right = 0, 0
    for l, r in segments:
        left -= k
        right += k
        left = max(left, l)
        right = min(right, r)
        if left > right:
            return False
    return True

def find_min_k(segments):
    lo, hi = 0, 10**9
    while lo < hi:
        mid = (lo + hi) // 2
        if can_complete(segments, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

t = int(input())
for _ in range(t):
    n = int(input())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    print(find_min_k(segments))
