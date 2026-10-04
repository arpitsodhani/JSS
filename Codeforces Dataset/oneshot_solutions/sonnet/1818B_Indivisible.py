def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 1:
            print(1)
        elif n % 2 == 1:
            print(-1)
        else:
            result = []
            for i in range(1, n + 1, 2):
                result.append(i + 1)
                result.append(i)
            print(' '.join(map(str, result)))

solve()
