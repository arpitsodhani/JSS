import sys
input = sys.stdin.readline

n, t = map(int, input().split())
a = list(map(int, input().split()))

current = 1
while current < t and current < n:
    current += a[current - 1]

if current == t:
    print("YES")
else:
    print("NO")
