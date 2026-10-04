a, x, y = map(int, input().split())

if 0 < x < a and 0 < y < a:
    print(0)
elif 0 <= x <= a and 0 <= y <= a:
    print(1)
else:
    print(2)
