import sys

# CLAUSE: validate_record_order
def validate_record_order(a):
    return len(a) > 0 and a[0] > 0 and all(a[i - 1] < a[i] for i in range(1, len(a)))

# CLAUSE: derive_primary_period
def derive_primary_period(a):
    period = a[0]
    return period

# CLAUSE: classify_primary_multiples
def classify_primary_multiples(a, period):
    flags = [False] * len(a)
    for i, x in enumerate(a):
        if x // period * period == x:
            flags[i] = True
    return flags

# CLAUSE: infer_secondary_period
def infer_secondary_period(a, flags):
    candidates = [x for x, ok in zip(a, flags) if not ok]
    return candidates[0] if candidates else None

# CLAUSE: merge_two_meeting_sequences
def merge_two_meeting_sequences(period, extra, amount):
    result = []
    i = 1
    j = 1
    while len(result) < amount:
        left = i * period
        right = j * extra if extra is not None else 10 ** 30
        take = left if left <= right else right
        result.append(take)
        if left == take:
            i += 1
        if right == take:
            j += 1
    return result

# CLAUSE: check_prefix_exactness
def check_prefix_exactness(a, period, extra):
    expected = merge_two_meeting_sequences(period, extra, len(a))
    return expected == a

# CLAUSE: handle_degenerate_speed_cases
def handle_degenerate_speed_cases(period, extra):
    return extra is None or period < extra

def possible(a):
    if not validate_record_order(a):
        return False
    period = derive_primary_period(a)
    flags = classify_primary_multiples(a, period)
    extra = infer_secondary_period(a, flags)
    if not handle_degenerate_speed_cases(period, extra):
        return False
    return check_prefix_exactness(a, period, extra)

def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    p = 1
    res = []
    for _ in range(t):
        n = int(raw[p])
        p += 1
        a = [int(x) for x in raw[p:p + n]]
        p += n
        res.append("VALID" if possible(a) else "INVALID")
    print("\n".join(res))

if __name__ == "__main__":
    main()
