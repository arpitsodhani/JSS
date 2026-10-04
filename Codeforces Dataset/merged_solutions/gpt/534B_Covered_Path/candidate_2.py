# CLAUSE: parse_path_parameters
import sys

data = tuple(map(int, sys.stdin.buffer.read().split()))
v1, v2, t, d = data

# CLAUSE: derive_speed_envelope
left_start = v1
right_finish = v2
seconds = t
step = d

# CLAUSE: compute_per_second_limits
limits = []
for second in range(seconds):
    start_limit = left_start + second * step
    finish_limit = right_finish + (seconds - second - 1) * step
    limits.append((start_limit, finish_limit))

# CLAUSE: choose_maximal_feasible_speed
chosen = []
for pair in limits:
    chosen.append(pair[0] if pair[0] < pair[1] else pair[1])

# CLAUSE: accumulate_covered_distance
answer = 0
for speed in chosen:
    answer += speed

# CLAUSE: validate_endpoint_constraints
if chosen[0] != v1 or chosen[-1] != v2:
    raise RuntimeError
for previous, current in zip(chosen, chosen[1:]):
    if abs(current - previous) > d:
        raise RuntimeError

print(answer)
