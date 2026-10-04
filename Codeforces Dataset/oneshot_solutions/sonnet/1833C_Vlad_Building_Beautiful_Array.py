import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    min_odd = None
    min_even = None
    
    for x in a:
        if x % 2 == 1:
            if min_odd is None or x < min_odd:
                min_odd = x
        else:
            if min_even is None or x < min_even:
                min_even = x
    
    if min_odd is None or min_even is None or min_even > min_odd:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()
