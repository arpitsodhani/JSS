import sys

# CLAUSE: validate_record_order
def validate_record_order(times):
    if not times:
        return False
    low = 0
    for time in times:
        if time <= low:
            return False
        low = time
    return True

# CLAUSE: derive_primary_period
def derive_primary_period(times):
    primary = times[0]
    return primary

# CLAUSE: classify_primary_multiples
def classify_primary_multiples(times, primary):
    explained = {}
    for i, time in enumerate(times):
        explained[i] = (time % primary == 0)
    return explained

# CLAUSE: infer_secondary_period
def infer_secondary_period(times, explained):
    for i in range(len(times)):
        if not explained[i]:
            return times[i]
    return None

# CLAUSE: merge_two_meeting_sequences
def merge_two_meeting_sequences(primary, secondary, count):
    answer = []
    next_primary = primary
    next_secondary = secondary
    while len(answer) < count:
        if next_secondary is None or next_primary < next_secondary:
            answer.append(next_primary)
            next_primary += primary
        elif next_secondary < next_primary:
            answer.append(next_secondary)
            next_secondary += secondary
        else:
            answer.append(next_primary)
            next_primary += primary
            next_secondary += secondary
    return answer

# CLAUSE: check_prefix_exactness
def check_prefix_exactness(times, primary, secondary):
    expected = merge_two_meeting_sequences(primary, secondary, len(times))
    pos = 0
    while pos < len(times):
        if times[pos] != expected[pos]:
            return False
        pos += 1
    return True

# CLAUSE: handle_degenerate_speed_cases
def handle_degenerate_speed_cases(primary, secondary):
    if secondary is None:
        return True
    if secondary <= primary:
        return False
    return True

def is_valid(times):
    if not validate_record_order(times):
        return False
    primary = derive_primary_period(times)
    explained = classify_primary_multiples(times, primary)
    secondary = infer_secondary_period(times, explained)
    if not handle_degenerate_speed_cases(primary, secondary):
        return False
    return check_prefix_exactness(times, primary, secondary)

def main():
    stream = iter(map(int, sys.stdin.buffer.read().split()))
    test_count = next(stream)
    out = []
    for _ in range(test_count):
        n = next(stream)
        times = [next(stream) for _ in range(n)]
        out.append("VALID" if is_valid(times) else "INVALID")
    print("\n".join(out))

if __name__ == "__main__":
    main()
