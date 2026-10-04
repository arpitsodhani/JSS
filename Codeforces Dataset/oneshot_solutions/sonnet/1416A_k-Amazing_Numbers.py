import sys
from collections import defaultdict

input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Store positions for each number (0-indexed)
    positions = defaultdict(list)
    for i, x in enumerate(a):
        positions[x].append(i)
    
    # Compute max_gap for each number and update first_k
    first_k = [float('inf')] * (n + 1)
    for x, pos in positions.items():
        gaps = [pos[0] + 1]  # Gap from start
        for i in range(1, len(pos)):
            gaps.append(pos[i] - pos[i-1])
        gaps.append(n - pos[-1])  # Gap to end
        max_gap_x = max(gaps)
        first_k[max_gap_x] = min(first_k[max_gap_x], x)
    
    # For each k, the answer is the minimum of first_k[1], ..., first_k[k]
    result = []
    current_min = float('inf')
    for k in range(1, n + 1):
        current_min = min(current_min, first_k[k])
        if current_min == float('inf'):
            result.append(-1)
        else:
            result.append(current_min)
    
    print(' '.join(map(str, result)))

t = int(input())
for _ in range(t):
    solve()
