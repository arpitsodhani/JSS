import sys

# CLAUSE: map_target_indices
def map_target_indices(items):
    tracked = [0] * len(items)
    for i in range(len(items)):
        tracked[i] = items[i]
    return tracked

# CLAUSE: reverse_query_order
def reverse_query_order(queries):
    return range(len(queries) - 1, -1, -1)

# CLAUSE: classify_query_effect
def classify_query_effect(position, left, right):
    return left <= position and position <= right

# CLAUSE: invert_cyclic_shift
def invert_cyclic_shift(position, left, right):
    if position == left:
        position = right
    else:
        position -= 1
    return position

# CLAUSE: invert_segment_reverse
def invert_segment_reverse(position, left, right):
    return left + (right - position)

# CLAUSE: update_tracked_positions
def update_tracked_positions(positions, queries, query_index):
    query_type, left, right = queries[query_index]
    i = 0
    while i < len(positions):
        position = positions[i]
        if classify_query_effect(position, left, right):
            if query_type == 1:
                positions[i] = invert_cyclic_shift(position, left, right)
            else:
                positions[i] = invert_segment_reverse(position, left, right)
        i += 1

# CLAUSE: extract_final_values
def extract_final_values(array, positions):
    out = [None] * len(positions)
    for i in range(len(positions)):
        out[i] = str(array[positions[i]])
    return " ".join(out)

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    n = nums[p]
    q = nums[p + 1]
    m = nums[p + 2]
    p += 3
    array = nums[p:p + n]
    array.insert(0, 0)
    p += n
    queries = []
    add_query = queries.append
    for _ in range(q):
        add_query((nums[p], nums[p + 1], nums[p + 2]))
        p += 3
    positions = map_target_indices(nums[p:p + m])
    for query_index in reverse_query_order(queries):
        update_tracked_positions(positions, queries, query_index)
    sys.stdout.write(extract_final_values(array, positions))

if __name__ == "__main__":
    main()
