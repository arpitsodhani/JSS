import sys

t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    
    if n % 2 == 1:
        print("NO")
    else:
        mid = n // 2
        if s[:mid] == s[mid:]:
            print("YES")
        else:
            print("NO")
