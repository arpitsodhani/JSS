# CLAUSE: setup_environment
import sys
from bisect import bisect_left

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    intervals = []
    coords = []

    p = 1
    for i in range(n):
        l = data[p]
        r = data[p + 1]
        p += 2
        intervals.append((l, r))
        coords.append(l)
        coords.append(r + 1)

    coords = sorted(set(coords))
    m = len(coords)

    diff = [0] * (m + 1)
    indexed = []

    for l, r in intervals:
        a = bisect_left(coords, l)
        b = bisect_left(coords, r + 1)
        indexed.append((a, b))
        diff[a] += 1
        diff[b] -= 1

    single_prefix = [0] * m
    cur = 0
    for i in range(m - 1):
        cur += diff[i]
        single_prefix[i + 1] = single_prefix[i] + (1 if cur == 1 else 0)

    for i, (a, b) in enumerate(indexed, 1):
        if single_prefix[b] - single_prefix[a] == 0:
            print(i)
            return

    print(-1)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
