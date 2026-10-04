import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    islands = []
    for _ in range(n):
        l, r = map(int, input().split())
        islands.append((l, r))
    
    bridges = list(map(int, input().split()))
    
    # Calculate gaps with their acceptable bridge length ranges
    gaps = []
    for i in range(n - 1):
        min_len = islands[i + 1][0] - islands[i][1]
        max_len = islands[i + 1][1] - islands[i][0]
        gaps.append((max_len, min_len, i))
    
    # Sort gaps by max_len (process constrained gaps first)
    gaps.sort()
    
    # Create sorted list of (bridge_length, original_index)
    bridge_list = [(bridges[i], i) for i in range(m)]
    bridge_list.sort()
    
    result = [0] * (n - 1)
    available = bridge_list[:]
    
    for max_len, min_len, gap_idx in gaps:
        # Binary search for the first bridge >= min_len
        lo, hi = 0, len(available)
        while lo < hi:
            mid = (lo + hi) // 2
            if available[mid][0] >= min_len:
                hi = mid
            else:
                lo = mid + 1
        
        # Check if found bridge is within max_len
        if lo < len(available) and available[lo][0] <= max_len:
            result[gap_idx] = available[lo][1] + 1  # 1-indexed
            available.pop(lo)
        else:
            print("No")
            return
    
    print("Yes")
    print(' '.join(map(str, result)))

main()
