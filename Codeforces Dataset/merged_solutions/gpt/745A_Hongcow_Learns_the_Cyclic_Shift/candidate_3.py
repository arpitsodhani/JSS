import sys

word = sys.stdin.readline().rstrip("\n")
length = len(word)

# CLAUSE: canonicalize_rotation_window
cyclic_space = word + word

# CLAUSE: enumerate_cyclic_offsets
unique_rotations = set()
index = 0
while index < length:
    # CLAUSE: construct_shift_signature
    candidate = cyclic_space[index:index + length]

    # CLAUSE: record_unique_rotation
    unique_rotations.add(candidate)
    index += 1

# CLAUSE: count_distinct_rotations
print(len(unique_rotations))
