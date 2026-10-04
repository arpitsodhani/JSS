n = int(input())

board = []
count = 0

for i in range(n):
    row = []
    for j in range(n):
        if (i + j) % 2 == 0:
            row.append('C')
            count += 1
        else:
            row.append('.')
    board.append(''.join(row))

print(count)
for row in board:
    print(row)
