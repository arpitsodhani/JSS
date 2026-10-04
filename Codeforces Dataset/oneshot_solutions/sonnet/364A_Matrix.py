import sys
from collections import defaultdict

def solve():
    lines = sys.stdin.read().strip().split('\n')
    a = int(lines[0])
    s = lines[1]
    
    n = len(s)
    digits = [int(c) for c in s]
    
    # Compute prefix sums for efficient range sum queries
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + digits[i]
    
    # Count frequency of each contiguous subsequence sum
    count = defaultdict(int)
    for i in range(n):
        for j in range(i, n):
            subsum = prefix[j + 1] - prefix[i]
            count[subsum] += 1
    
    # Count rectangles with sum = a
    result = 0
    if a == 0:
        # Special case: need r*c = 0, so r=0 or c=0
        total_count = sum(count.values())
        result = count[0] * (2 * total_count - count[0])
    else:
        # Iterate over divisors of a
        d = 1
        while d * d <= a:
            if a % d == 0:
                d2 = a // d
                if d == d2:
                    result += count[d] * count[d]
                else:
                    result += 2 * count[d] * count[d2]
            d += 1
    
    print(result)

solve()
