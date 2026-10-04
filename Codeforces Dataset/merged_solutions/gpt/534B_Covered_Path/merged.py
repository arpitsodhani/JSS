# Clause parse_path_parameters [Confidence: 0.40]
import sys

def parse_path_parameters():
    tokens = iter(map(int, sys.stdin.read().split()))
    return next(tokens), next(tokens), next(tokens), next(tokens)


# Clause derive_speed_envelope [Confidence: 0.40]
def derive_speed_envelope(v1, v2, t, d):
    indexes = range(t)
    remaining = range(t - 1, -1, -1)
    return indexes, remaining


# Clause compute_per_second_limits [Confidence: 0.40]
def compute_per_second_limits(forward_start, backward_start, d, t):
    current_forward = forward_start
    current_backward = backward_start
    result = []
    for _ in range(t):
        result.append((current_forward, current_backward))
        current_forward += d
        current_backward -= d
    return result


# Clause choose_maximal_feasible_speed [Confidence: 0.20]
def choose_maximal_feasible_speed(per_second):
    speeds = []
    for start_bound, end_bound in per_second:
        speeds.append(min(start_bound, end_bound))
    return speeds


# Clause accumulate_covered_distance [Confidence: 0.40]
def accumulate_covered_distance(speeds):
    return sum(speeds)


# Clause validate_endpoint_constraints [Confidence: 0.60]
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


