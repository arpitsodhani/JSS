import sys

s = sys.stdin.read().strip()
n = len(s)

# CLAUSE: canonicalize_rotation_window
window_source = s + s

# CLAUSE: enumerate_cyclic_offsets
seen = set()
for pos in range(0, n):
    # CLAUSE: construct_shift_signature
    rotation = window_source[pos:pos + n]

    # CLAUSE: record_unique_rotation
    seen.add(rotation)

# CLAUSE: count_distinct_rotations
answer = len(seen)
sys.stdout.write(str(answer))
