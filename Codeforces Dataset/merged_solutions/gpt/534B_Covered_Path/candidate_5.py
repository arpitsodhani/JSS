# CLAUSE: parse_path_parameters
import sys

numbers = [int(x) for x in sys.stdin.buffer.read().split()]
v1 = numbers[0]
v2 = numbers[1]
t = numbers[2]
d = numbers[3]

# CLAUSE: derive_speed_envelope
forward_origin = v1
backward_origin = v2
last_index = t - 1

# CLAUSE: compute_per_second_limits
forward_limits = []
backward_limits = []
i = 0
while i < t:
    forward_limits.append(forward_origin + i * d)
    backward_limits.append(backward_origin + (last_index - i) * d)
    i += 1

# CLAUSE: choose_maximal_feasible_speed
speeds = [0] * t
for i in range(t):
    if forward_limits[i] <= backward_limits[i]:
        speeds[i] = forward_limits[i]
    else:
        speeds[i] = backward_limits[i]

# CLAUSE: accumulate_covered_distance
distance = sum(speeds)

# CLAUSE: validate_endpoint_constraints
assert speeds[0] == v1 and speeds[t - 1] == v2
for i in range(t - 1):
    assert abs(speeds[i + 1] - speeds[i]) <= d

print(distance)
