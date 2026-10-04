import sys

data = list(map(int, sys.stdin.read().split()))
n, k = data[0], data[1]
raw = data[2:2 + n]

# CLAUSE: normalize_table_state
available = raw

# CLAUSE: map_arrow_position
start = k - 1

# CLAUSE: traverse_clockwise_offsets
answer_index = start
for offset in range(n):
    current = (start + offset) % n

    # CLAUSE: test_question_availability
    can_choose = available[current] == 1

    # CLAUSE: select_first_unasked_sector
    if can_choose:
        answer_index = current
        break

# CLAUSE: restore_one_based_answer
print(answer_index + 1)
