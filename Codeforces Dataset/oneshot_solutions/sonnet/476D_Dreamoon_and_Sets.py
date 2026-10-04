import sys

def solve():
    k, n = map(int, sys.stdin.readline().split())
    
    m = k * (6 * n - 1)
    print(m)
    
    for i in range(n):
        a = k * (6 * i + 1)
        b = k * (6 * i + 2)
        c = k * (6 * i + 3)
        d = k * (6 * i + 5)
        print(a, b, c, d)

solve()
