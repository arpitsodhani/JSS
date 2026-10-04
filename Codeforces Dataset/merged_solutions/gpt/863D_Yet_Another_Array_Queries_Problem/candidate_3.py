import sys

# CLAUSE: map_target_indices
def map_target_indices(data, start, count):
    positions = []
    for offset in range(count):
        positions.append(data[start + offset])
    return positions

# CLAUSE: reverse_query_order
def reverse_query_order(queries):
    index = len(queries) - 1
    while index >= 0:
        yield queries[index]
        index -= 1

# CLAUSE: classify_query_effect
def classify_query_effect(position, bounds):
    left, right = bounds
    return left <= position <= right

# CLAUSE: invert_cyclic_shift
def invert_cyclic_shift(position, bounds):
    left, right = bounds
    if position > left:
        return position - 1
    return right

# CLAUSE: invert_segment_reverse
def invert_segment_reverse(position, bounds):
    left, right = bounds
    return left + right - position

# CLAUSE: update_tracked_positions
def update_tracked_positions(positions, operation):
    query_type, left, right = operation
    bounds = (left, right)
    for index in range(len(positions)):
        current = positions[index]
        if classify_query_effect(current, bounds):
            if query_type == 1:
                current = invert_cyclic_shift(current, bounds)
            else:
                current = invert_segment_reverse(current, bounds)
            positions[index] = current

# CLAUSE: extract_final_values
def extract_final_values(array, positions):
    return " ".join(str(array[position]) for position in positions)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    cursor = 0
    n = data[cursor]
    q = data[cursor + 1]
    m = data[cursor + 2]
    cursor += 3
    array = [0]
    array.extend(data[cursor:cursor + n])
    cursor += n
    queries = [None] * q
    for i in range(q):
        queries[i] = (data[cursor], data[cursor + 1], data[cursor + 2])
        cursor += 3
    positions = map_target_indices(data, cursor, m)
    for operation in reverse_query_order(queries):
        update_tracked_positions(positions, operation)
    sys.stdout.write(extract_final_values(array, positions))

if __name__ == "__main__":
    main()
