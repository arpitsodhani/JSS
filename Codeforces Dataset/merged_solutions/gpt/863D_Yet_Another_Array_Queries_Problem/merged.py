import sys

# CLAUSE: map_target_indices
def map_target_indices(raw_indices):
    return raw_indices[:]

# CLAUSE: reverse_query_order
def reverse_query_order(queries):
    return reversed(queries)

# CLAUSE: classify_query_effect
def classify_query_effect(position, left, right):
    return left <= position <= right

# CLAUSE: invert_cyclic_shift
def invert_cyclic_shift(position, left, right):
    if position == left:
        return right
    return position - 1

# CLAUSE: invert_segment_reverse
def invert_segment_reverse(position, left, right):
    return left + right - position

# CLAUSE: update_tracked_positions
def update_tracked_positions(positions, query):
    kind, left, right = query
    for i, position in enumerate(positions):
        if classify_query_effect(position, left, right):
            if kind == 1:
                positions[i] = invert_cyclic_shift(position, left, right)
            else:
                positions[i] = invert_segment_reverse(position, left, right)

# CLAUSE: extract_final_values
def extract_final_values(array, positions):
    return [array[position] for position in positions]

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    n, q, m = data[ptr], data[ptr + 1], data[ptr + 2]
    ptr += 3
    array = [0] + data[ptr:ptr + n]
    ptr += n
    queries = []
    for _ in range(q):
        queries.append((data[ptr], data[ptr + 1], data[ptr + 2]))
        ptr += 3
    positions = map_target_indices(data[ptr:ptr + m])
    for query in reverse_query_order(queries):
        update_tracked_positions(positions, query)
    print(*extract_final_values(array, positions))

if __name__ == "__main__":
    main()
