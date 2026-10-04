import sys

# CLAUSE: map_target_indices
def map_target_indices(values):
    return [value - 1 for value in values]

# CLAUSE: reverse_query_order
def reverse_query_order(types, lefts, rights):
    for index in range(len(types) - 1, -1, -1):
        yield types[index], lefts[index], rights[index]

# CLAUSE: classify_query_effect
def classify_query_effect(position, left, right):
    return not (position < left or position > right)

# CLAUSE: invert_cyclic_shift
def invert_cyclic_shift(position, left, right):
    return right if position == left else position - 1

# CLAUSE: invert_segment_reverse
def invert_segment_reverse(position, left, right):
    return right - (position - left)

# CLAUSE: update_tracked_positions
def update_tracked_positions(positions, query_type, left, right):
    updated = []
    for position in positions:
        if not classify_query_effect(position, left, right):
            updated.append(position)
        elif query_type == 1:
            updated.append(invert_cyclic_shift(position, left, right))
        else:
            updated.append(invert_segment_reverse(position, left, right))
    return updated

# CLAUSE: extract_final_values
def extract_final_values(array, positions):
    answer = []
    for position in positions:
        answer.append(array[position])
    return answer

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    n, q, m = tokens[at], tokens[at + 1], tokens[at + 2]
    at += 3
    array = tokens[at:at + n]
    at += n
    types, lefts, rights = [], [], []
    for _ in range(q):
        types.append(tokens[at])
        lefts.append(tokens[at + 1] - 1)
        rights.append(tokens[at + 2] - 1)
        at += 3
    positions = map_target_indices(tokens[at:at + m])
    for query_type, left, right in reverse_query_order(types, lefts, rights):
        positions = update_tracked_positions(positions, query_type, left, right)
    sys.stdout.write(" ".join(map(str, extract_final_values(array, positions))))

if __name__ == "__main__":
    main()
