import sys

s = sys.stdin.readline().strip()
n = len(s)

# CLAUSE: canonicalize_rotation_window
doubled = s + s

# CLAUSE: enumerate_cyclic_offsets
offsets = range(n)

# CLAUSE: construct_shift_signature
rotations = []
for start in offsets:
    rotations.append(doubled[start:start + n])

# CLAUSE: record_unique_rotation
unique = set(rotations)

# CLAUSE: count_distinct_rotations
print(len(unique))
