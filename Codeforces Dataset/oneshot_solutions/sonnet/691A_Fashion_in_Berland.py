n = int(input())
buttons = list(map(int, input().split()))

if n == 1:
    print("YES" if sum(buttons) == 1 else "NO")
else:
    print("YES" if sum(buttons) == n - 1 else "NO")
