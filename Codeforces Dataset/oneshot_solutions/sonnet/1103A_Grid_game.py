s = input().strip()
row = 1
col = 1

for c in s:
    print(row, col)
    if c == '0':  # vertical: 2x1 (2 rows, 1 column)
        col += 1
    else:  # horizontal: 1x2 (1 row, 2 columns)
        col += 2
    
    if col > 4:
        row = 3 if row == 1 else 1
        col = 1
