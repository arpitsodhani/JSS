import sys

def read_input():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    return nums[0], nums[1], nums[2:2 + nums[0]]

def scan(n, k, arr):
    # CLAUSE: normalize_table_state
    state = tuple(arr)

    # CLAUSE: map_arrow_position
    start_index = k - 1

    # CLAUSE: traverse_clockwise_offsets
    for i in range(n):
        candidate = start_index + i
        if candidate >= n:
            candidate -= n

        # CLAUSE: test_question_availability
        open_sector = state[candidate] == 1

        # CLAUSE: select_first_unasked_sector
        if open_sector:
            return candidate

n, k, arr = read_input()
chosen_index = scan(n, k, arr)

# CLAUSE: restore_one_based_answer
print(chosen_index + 1)
