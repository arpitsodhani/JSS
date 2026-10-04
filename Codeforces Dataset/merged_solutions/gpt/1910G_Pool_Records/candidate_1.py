import sys

# CLAUSE: validate_record_order
def validate_record_order(times):
    if not times or times[0] <= 0:
        return False
    for i in range(1, len(times)):
        if times[i] <= times[i - 1]:
            return False
    return True

# CLAUSE: derive_primary_period
def derive_primary_period(times):
    return times[0]

# CLAUSE: classify_primary_multiples
def classify_primary_multiples(times, primary):
    return [value % primary == 0 for value in times]

# CLAUSE: infer_secondary_period
def infer_secondary_period(times, primary_marks):
    for value, marked in zip(times, primary_marks):
        if not marked:
            return value
    return None

# CLAUSE: merge_two_meeting_sequences
def merge_two_meeting_sequences(primary, secondary, need):
    out = []
    a = primary
    b = secondary if secondary is not None else None
    while len(out) < need:
        if b is None or a < b:
            out.append(a)
            a += primary
        elif b < a:
            out.append(b)
            b += secondary
        else:
            out.append(a)
            a += primary
            b += secondary
    return out

# CLAUSE: check_prefix_exactness
def check_prefix_exactness(times, primary, secondary):
    return merge_two_meeting_sequences(primary, secondary, len(times)) == times

# CLAUSE: handle_degenerate_speed_cases
def handle_degenerate_speed_cases(primary, secondary):
    return secondary is None or secondary > primary

def valid(times):
    if not validate_record_order(times):
        return False
    primary = derive_primary_period(times)
    marks = classify_primary_multiples(times, primary)
    secondary = infer_secondary_period(times, marks)
    return handle_degenerate_speed_cases(primary, secondary) and check_prefix_exactness(times, primary, secondary)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    tests = data[0]
    pos = 1
    ans = []
    for _ in range(tests):
        n = data[pos]
        pos += 1
        arr = data[pos:pos + n]
        pos += n
        ans.append("VALID" if valid(arr) else "INVALID")
    print("\n".join(ans))

if __name__ == "__main__":
    main()
