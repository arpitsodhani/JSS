# CLAUSE: parse_path_parameters
import sys

def parse_path_parameters():
    tokens = iter(map(int, sys.stdin.read().split()))
    return next(tokens), next(tokens), next(tokens), next(tokens)

# CLAUSE: derive_speed_envelope
def derive_speed_envelope(v1, v2, t, d):
    forward_start = v1
    backward_start = v2 + (t - 1) * d
    return forward_start, backward_start, d

# CLAUSE: compute_per_second_limits
def compute_per_second_limits(forward_start, backward_start, d, t):
    current_forward = forward_start
    current_backward = backward_start
    result = []
    for _ in range(t):
        result.append((current_forward, current_backward))
        current_forward += d
        current_backward -= d
    return result

# CLAUSE: choose_maximal_feasible_speed
def choose_maximal_feasible_speed(limits):
    return list(map(lambda bounds: min(bounds[0], bounds[1]), limits))

# CLAUSE: accumulate_covered_distance
def accumulate_covered_distance(speeds):
    total = sum(speeds)
    return total

# CLAUSE: validate_endpoint_constraints
def validate_endpoint_constraints(speeds, v1, v2, d):
    assert speeds[:1] == [v1]
    assert speeds[-1:] == [v2]
    assert max((abs(a - b) for a, b in zip(speeds, speeds[1:])), default=0) <= d

v1, v2, t, d = parse_path_parameters()
forward_start, backward_start, delta = derive_speed_envelope(v1, v2, t, d)
limits = compute_per_second_limits(forward_start, backward_start, delta, t)
speeds = choose_maximal_feasible_speed(limits)
validate_endpoint_constraints(speeds, v1, v2, d)
print(accumulate_covered_distance(speeds))
