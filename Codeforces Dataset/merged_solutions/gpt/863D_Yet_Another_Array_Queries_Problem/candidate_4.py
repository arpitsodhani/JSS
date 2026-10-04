import sys

# CLAUSE: map_target_indices
def map_target_indices(indices):
    return list(indices)

# CLAUSE: reverse_query_order
def reverse_query_order(queries):
    return queries[::-1]

# CLAUSE: classify_query_effect
def classify_query_effect(position, left, right):
    if position < left:
        return False
    if position > right:
        return False
    return True

# CLAUSE: invert_cyclic_shift
def invert_cyclic_shift(position, left, right):
    moved_from_end = position == left
    return right if moved_from_end else position - 1

# CLAUSE: invert_segment_reverse
def invert_segment_reverse(position, left, right):
    distance_from_left = position - left
    return right - distance_from_left

# CLAUSE: update_tracked_positions
def update_tracked_positions(positions, query):
    query_type = query[0]
    left = query[1]
    right = query[2]
    result = positions[:]
    for index, position in enumerate(positions):
        if classify_query_effect(position, left, right):
            if query_type == 1:
                result[index] = invert_cyclic_shift(position, left, right)
            else:
                result[index] = invert_segment_reverse(position, left, right)
    return result

# CLAUSE: extract_final_values
def extract_final_values(array, positions):
    values = []
    append = values.append
    for position in positions:
        append(str(array[position]))
    return values

def main():
    raw = sys.stdin.buffer.read().split()
    n, q, m = map(int, raw[:3])
    array = [0] + list(map(int, raw[3:3 + n]))
    base = 3 + n
    queries = []
    for i in range(q):
        j = base + 3 * i
        queries.append(tuple(map(int, raw[j:j + 3])))
    important_start = base + 3 * q
    positions = map_target_indices(map(int, raw[important_start:important_start + m]))
    for query in reverse_query_order(queries):
        positions = update_tracked_positions(positions, query)
    sys.stdout.write(" ".join(extract_final_values(array, positions)))

if __name__ == "__main__":
    main()
