t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(-1)
    else:
        result = [(2 * (j - 1) % n) + 1 for j in range(1, n + 1)]
        print(' '.join(map(str, result)))
