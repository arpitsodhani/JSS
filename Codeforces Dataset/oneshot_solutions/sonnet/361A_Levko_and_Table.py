n, k = map(int, input().split())
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(k)
        else:
            row.append(0)
    print(' '.join(map(str, row)))
