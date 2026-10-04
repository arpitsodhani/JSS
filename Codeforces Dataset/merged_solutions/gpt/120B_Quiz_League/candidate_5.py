import sys

data = [int(part) for part in sys.stdin.read().split()]
n = data[0]
k = data[1]

# CLAUSE: normalize_table_state
availability = data[2:2 + n]

# CLAUSE: map_arrow_position
cursor = k

# CLAUSE: traverse_clockwise_offsets
checked = 0
result = k
while checked != n:
    if cursor > n:
        cursor = 1

    # CLAUSE: test_question_availability
    usable = availability[cursor - 1] == 1

    # CLAUSE: select_first_unasked_sector
    if usable:
        result = cursor
        break
    cursor += 1
    checked += 1

# CLAUSE: restore_one_based_answer
sys.stdout.write(f"{result}\n")
