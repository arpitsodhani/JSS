t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    for i in range(n):
        if i == 0:
            print('W' + 'B' * (m - 1))
        else:
            print('B' * m)
