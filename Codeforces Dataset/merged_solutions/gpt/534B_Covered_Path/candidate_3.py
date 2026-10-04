# CLAUSE: parse_path_parameters
import sys

def parse_path_parameters():
    raw = sys.stdin.readline().split() + sys.stdin.readline().split()
    v1, v2, t, d = map(int, raw)
    return v1, v2, t, d

# CLAUSE: derive_speed_envelope
def derive_speed_envelope(v1, v2, t, d):
    indexes = range(t)
    remaining = range(t - 1, -1, -1)
    return indexes, remaining

# CLAUSE: compute_per_second_limits
def compute_per_second_limits(indexes, remaining, v1, v2, d):
    per_second = []
    for from_start, to_end in zip(indexes, remaining):
        per_second.append((v1 + from_start * d, v2 + to_end * d))
    return per_second

# CLAUSE: choose_maximal_feasible_speed
def choose_maximal_feasible_speed(per_second):
    speeds = []
    for start_bound, end_bound in per_second:
        speeds.append(min(start_bound, end_bound))
    return speeds

# CLAUSE: accumulate_covered_distance
def accumulate_covered_distance(speeds):
    total = 0
    for value in speeds:
        total += value
    return total

# CLAUSE: validate_endpoint_constraints
def validate_endpoint_constraints(speeds, v1, v2, d):
    ok = speeds and speeds[0] == v1 and speeds[-1] == v2
    ok = ok and all(abs(speeds[i] - speeds[i - 1]) <= d for i in range(1, len(speeds)))
    if not ok:
        raise AssertionError

v1, v2, t, d = parse_path_parameters()
indexes, remaining = derive_speed_envelope(v1, v2, t, d)
per_second = compute_per_second_limits(indexes, remaining, v1, v2, d)
speeds = choose_maximal_feasible_speed(per_second)
validate_endpoint_constraints(speeds, v1, v2, d)
print(accumulate_covered_distance(speeds))
