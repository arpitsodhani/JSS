n, m, k = map(int, input().split())

# Generate snake path through all cells
cells = []
for i in range(1, n + 1):
    if i % 2 == 1:  # odd rows: left to right
        for j in range(1, m + 1):
            cells.append((i, j))
    else:  # even rows: right to left
        for j in range(m, 0, -1):
            cells.append((i, j))

# Split into k tubes
idx = 0
for tube_num in range(k):
    if tube_num < k - 1:
        tube_size = 2
    else:
        tube_size = len(cells) - idx
    
    # Output this tube
    result = [str(tube_size)]
    for i in range(tube_size):
        x, y = cells[idx]
        result.append(str(x))
        result.append(str(y))
        idx += 1
    print(' '.join(result))
