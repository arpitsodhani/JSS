import sys

def solve():
    n, m = map(int, input().split())
    seats = list(map(int, input().split()))
    
    L = sum(1 for s in seats if s == -1)
    R = sum(1 for s in seats if s == -2)
    specific = [s for s in seats if s > 0 and s <= m]
    specific_set = sorted(set(specific))
    
    max_seated = min(L + R, m)
    
    if specific_set:
        for i, min_s in enumerate(specific_set):
            for j in range(i, len(specific_set)):
                max_s = specific_set[j]
                
                best_l = 0
                for l in range(min(L, min_s - 1) + 1):
                    left_overlap = sum(1 for s in specific_set if min_s - l <= s < min_s)
                    best_l = max(best_l, l - left_overlap)
                
                best_r = 0
                for r in range(min(R, m - max_s) + 1):
                    right_overlap = sum(1 for s in specific_set if max_s < s <= max_s + r)
                    best_r = max(best_r, r - right_overlap)
                
                total = best_l + best_r + len(specific_set)
                max_seated = max(max_seated, total)
    
    return max_seated

t = int(input())
for _ in range(t):
    print(solve())
