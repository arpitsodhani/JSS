import sys

s = sys.stdin.readline().strip()
n = len(s)

# CLAUSE: canonicalize_rotation_window
extended = s + s

# CLAUSE: enumerate_cyclic_offsets
distinct_rotations = []
seen = set()
for start in range(n):
    # CLAUSE: construct_shift_signature
    formed = extended[start:start + n]

    # CLAUSE: record_unique_rotation
    if formed not in seen:
        seen.add(formed)
        distinct_rotations.append(formed)

# CLAUSE: count_distinct_rotations
print(len(distinct_rotations))
