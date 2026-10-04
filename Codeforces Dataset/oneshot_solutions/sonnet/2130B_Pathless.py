import sys
input = sys.stdin.readline

def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    
    c0 = a.count(0)
    c1 = a.count(1)
    c2 = a.count(2)
    
    S_min = c1 + 2 * c2
    
    if s < S_min:
        result = [0] * c0 + [1] * c1 + [2] * c2
        print(' '.join(map(str, result)))
    elif s == S_min + 1:
        result = [0] * c0 + [2] * c2 + [1] * c1
        print(' '.join(map(str, result)))
    else:
        print(-1)

t = int(input())
for _ in range(t):
    solve()
