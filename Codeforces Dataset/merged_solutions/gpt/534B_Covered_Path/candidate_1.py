# CLAUSE: parse_path_parameters
import sys

def parse_path_parameters():
    values = list(map(int, sys.stdin.read().split()))
    return values[0], values[1], values[2], values[3]

# CLAUSE: derive_speed_envelope
def derive_speed_envelope(v1, v2, t, d):
    return v1, v2, t, d

# CLAUSE: compute_per_second_limits
def compute_per_second_limits(v1, v2, t, d):
    forward = [v1 + i * d for i in range(t)]
    backward = [v2 + (t - 1 - i) * d for i in range(t)]
    return forward, backward

# CLAUSE: choose_maximal_feasible_speed
def choose_maximal_feasible_speed(forward, backward):
    return [min(a, b) for a, b in zip(forward, backward)]

# CLAUSE: accumulate_covered_distance
def accumulate_covered_distance(speeds):
    return sum(speeds)

# CLAUSE: validate_endpoint_constraints
def validate_endpoint_constraints(speeds, v1, v2, d):
    assert speeds[0] == v1
    assert speeds[-1] == v2
    for i in range(1, len(speeds)):
        assert abs(speeds[i] - speeds[i - 1]) <= d

v1, v2, t, d = parse_path_parameters()
envelope = derive_speed_envelope(v1, v2, t, d)
forward, backward = compute_per_second_limits(*envelope)
speeds = choose_maximal_feasible_speed(forward, backward)
validate_endpoint_constraints(speeds, v1, v2, d)
print(accumulate_covered_distance(speeds))
