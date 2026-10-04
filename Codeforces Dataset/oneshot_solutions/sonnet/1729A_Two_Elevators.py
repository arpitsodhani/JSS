import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    time1 = abs(a - 1)
    time2 = abs(b - c) + abs(c - 1)
    
    if time1 < time2:
        print(1)
    elif time1 > time2:
        print(2)
    else:
        print(3)
