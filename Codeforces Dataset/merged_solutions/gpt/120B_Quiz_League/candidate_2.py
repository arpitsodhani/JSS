import sys

tokens = sys.stdin.buffer.read().split()
n = int(tokens[0])
k = int(tokens[1])
values = [int(x) for x in tokens[2:2 + n]]

# CLAUSE: normalize_table_state
table = [v == 1 for v in values]

# CLAUSE: map_arrow_position
pos = k - 1

# CLAUSE: traverse_clockwise_offsets
steps = 0
chosen = pos
while steps < n:
    # CLAUSE: test_question_availability
    is_unasked = table[pos]

    # CLAUSE: select_first_unasked_sector
    if is_unasked:
        chosen = pos
        break
    pos += 1
    if pos == n:
        pos = 0
    steps += 1

# CLAUSE: restore_one_based_answer
sys.stdout.write(str(chosen + 1))
