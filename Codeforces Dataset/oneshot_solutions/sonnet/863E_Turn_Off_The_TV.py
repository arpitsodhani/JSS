import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    intervals = []
    coords = []
    
    idx = 1
    for i in range(n):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        intervals.append((l, r))
        coords.append(l)
        coords.append(r + 1)
    
    coords = sorted(set(coords))
    m = len(coords)
    
    diff = [0] * (m + 1)
    for l, r in intervals:
        left = bisect_left(coords, l)
        right = bisect_left(coords, r + 1)
        diff[left] += 1
        diff[right] -= 1
    
    single_prefix = [0] * m
    cur = 0
    for i in range(m - 1):
        cur += diff[i]
        single_prefix[i + 1] = single_prefix[i] + (1 if cur == 1 else 0)
    
    for i, (l, r) in enumerate(intervals, 1):
        left = bisect_left(coords, l)
        right = bisect_left(coords, r + 1)
        if single_prefix[right] == single_prefix[left]:
            print(i)
            return
    
    print(-1)

if __name__ == "__main__":
    main()
