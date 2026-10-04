import sys

def solve():
    n = int(input())
    
    left, right = 1, n
    
    while left < right:
        mid = (left + right) // 2
        
        # Query [left, mid]
        print(f"? {left} {mid}")
        sys.stdout.flush()
        response = list(map(int, input().split()))
        
        # Count how many values are in [left, mid]
        count = sum(1 for x in response if left <= x <= mid)
        
        if count % 2 == 1:
            # Fixed point is in [left, mid]
            right = mid
        else:
            # Fixed point is in [mid+1, right]
            left = mid + 1
    
    print(f"! {left}")
    sys.stdout.flush()

t = int(input())
for _ in range(t):
    solve()
