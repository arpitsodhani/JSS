import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Find first and last occurrence of 0 (water)
    first_zero = -1
    last_zero = -1
    
    for i in range(n):
        if a[i] == 0:
            if first_zero == -1:
                first_zero = i
            last_zero = i
    
    if first_zero == -1:
        # No water, can walk for free
        return 0
    else:
        # Jump from (first_zero - 1) to (last_zero + 1)
        # Cost = distance = (last_zero + 1) - (first_zero - 1)
        return last_zero - first_zero + 2

t = int(input())
for _ in range(t):
    print(solve())
