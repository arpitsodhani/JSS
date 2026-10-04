import sys

s = sys.stdin.readline().strip()
n = len(s)

# CLAUSE: canonicalize_rotation_window
base = s + s

# CLAUSE: enumerate_cyclic_offsets
all_offsets = [i for i in range(n)]

# CLAUSE: construct_shift_signature
def rotation_at(i):
    return base[i:i + n]

# CLAUSE: record_unique_rotation
distinct = set()
for i in all_offsets:
    distinct.add(rotation_at(i))

# CLAUSE: count_distinct_rotations
print(len(distinct))
