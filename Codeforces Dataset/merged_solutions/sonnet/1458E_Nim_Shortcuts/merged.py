# Clause setup_environment [Confidence: 0.40]
import sys
import bisect


# Clause solve_logic [Confidence: 0.60]
raw = list(map(int, sys.stdin.buffer.read().split()))
n, m = raw[0], raw[1]
offset = 2

shortcut_rows = {}
shortcut_cells = set()
compressed_columns = []
for _ in range(n):
    x, y = raw[offset], raw[offset + 1]
    offset += 2
    shortcut_cells.add((x, y))
    shortcut_rows.setdefault(x, []).append(y)
    compressed_columns.append(y)

row_queries = {}
queries = []
event_rows = set(shortcut_rows)
for index in range(m):
    x, y = raw[offset], raw[offset + 1]
    offset += 2
    queries.append((x, y))
    row_queries.setdefault(x, []).append((index, y))
    event_rows.add(x)

compressed_columns = sorted(set(compressed_columns))
bit = [0] * (len(compressed_columns) + 1)
inserted = set()

def add_value(value):
    if value in inserted:
        return
    inserted.add(value)
    i = bisect_left(compressed_columns, value) + 1
    while i <= len(compressed_columns):
        bit[i] += 1
        i += i & -i

def bit_sum(i):
    result = 0
    while i:
        result += bit[i]
        i -= i & -i
    return result

def blocked_count(left, right):
    right_index = bisect_right(compressed_columns, right)
    left_index = bisect_left(compressed_columns, left)
    return bit_sum(right_index) - bit_sum(left_index)

def next_after_steps(start, steps):
    left = start
    right = start + steps + len(compressed_columns) + 3
    while left < right:
        middle = (left + right) // 2
        if middle - start + 1 - blocked_count(start, middle) >= steps:
            right = middle
        else:
            left = middle + 1
    return left

for value_list in shortcut_rows.values():
    value_list.sort()

answers = ["WIN"] * m
free_column = 0
done_row = -1

for row in sorted(event_rows):
    free_column = next_after_steps(free_column, row - done_row)

    values = shortcut_rows.get(row, [])
    first_value = values[0] if values else None
    cold_column = free_column if first_value is None or free_column < first_value else None

    for index, col in row_queries.get(row, []):
        if (row, col) in shortcut_cells or col == cold_column:
            answers[index] = "LOSE"

    if cold_column is not None:
        free_column = next_after_steps(free_column, 2)

    for col in values:
        add_value(col)

    free_column = next_after_steps(free_column, 1)
    done_row = row


# Clause finish_program [Confidence: 0.60]
sys.stdout.write("\n".join(answers))


