n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input())

count = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if (matrix[i][j] == 'X' and
            matrix[i-1][j-1] == 'X' and
            matrix[i-1][j+1] == 'X' and
            matrix[i+1][j-1] == 'X' and
            matrix[i+1][j+1] == 'X'):
            count += 1

print(count)
