def solve():
    n, m, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    accessible = set()
    pointer = 0
    
    for i in range(m):
        # Expose members until b[i] is accessible
        while b[i] not in accessible and pointer < n:
            accessible.add(a[pointer])
            pointer += 1
        
        if b[i] not in accessible:
            return "TIDAK"
    
    return "YA"

t = int(input())
for _ in range(t):
    print(solve())
