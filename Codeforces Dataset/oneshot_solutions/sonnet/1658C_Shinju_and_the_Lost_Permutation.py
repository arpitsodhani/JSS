import sys

def solve():
    n = int(input())
    c = list(map(int, input().split()))
    
    # Check minimum is 1 and appears exactly once
    if min(c) != 1:
        return "NO"
    
    if c.count(1) != 1:
        return "NO"
    
    idx = c.index(1)
    
    # Check from c[0] to c[idx-1]: non-decreasing with max increment 1
    for i in range(1, idx):
        if c[i] < c[i-1] or c[i] > c[i-1] + 1:
            return "NO"
    
    # Check from c[idx+1] to c[n-1]: non-decreasing with max increment 1
    for i in range(idx + 1, n):
        if c[i] < c[i-1] or c[i] > c[i-1] + 1:
            return "NO"
    
    return "YES"

t = int(input())
for _ in range(t):
    print(solve())
