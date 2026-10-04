import sys

items = list(map(int, sys.stdin.readline().split()))
while len(items) < 2:
    items += list(map(int, sys.stdin.readline().split()))
n, k = items[0], items[1]
while len(items) < n + 2:
    items += list(map(int, sys.stdin.readline().split()))

# CLAUSE: normalize_table_state
sectors = items[2:n + 2]

# CLAUSE: map_arrow_position
base = k - 1

# CLAUSE: traverse_clockwise_offsets
cycle = range(base, base + n)
selected = None
for absolute in cycle:
    idx = absolute % n

    # CLAUSE: test_question_availability
    available = sectors[idx] == 1

    # CLAUSE: select_first_unasked_sector
    if available:
        selected = idx
        break

# CLAUSE: restore_one_based_answer
print(selected + 1)
