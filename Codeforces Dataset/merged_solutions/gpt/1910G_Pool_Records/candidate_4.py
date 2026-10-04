import sys
from math import gcd

# CLAUSE: validate_record_order
def validate_record_order(seq):
    if len(seq) == 0 or seq[0] < 1:
        return False
    pairs = zip(seq, seq[1:])
    return all(x < y for x, y in pairs)

# CLAUSE: derive_primary_period
def derive_primary_period(seq):
    return seq[0]

# CLAUSE: classify_primary_multiples
def classify_primary_multiples(seq, small):
    return tuple(x % small == 0 for x in seq)

# CLAUSE: infer_secondary_period
def infer_secondary_period(seq, primary_ok):
    for idx in range(len(seq)):
        if not primary_ok[idx]:
            return seq[idx]
    return None

# CLAUSE: merge_two_meeting_sequences
def merge_two_meeting_sequences(small, large, limit):
    if large is None:
        return limit // small
    common = small // gcd(small, large) * large
    return limit // small + limit // large - limit // common

# CLAUSE: check_prefix_exactness
def check_prefix_exactness(seq, small, large):
    last = seq[-1]
    if merge_two_meeting_sequences(small, large, last) != len(seq):
        return False
    for x in seq:
        if x % small != 0 and (large is None or x % large != 0):
            return False
    return True

# CLAUSE: handle_degenerate_speed_cases
def handle_degenerate_speed_cases(small, large):
    return large is None or large > small

def judge(seq):
    if not validate_record_order(seq):
        return False
    small = derive_primary_period(seq)
    primary_ok = classify_primary_multiples(seq, small)
    large = infer_secondary_period(seq, primary_ok)
    if not handle_degenerate_speed_cases(small, large):
        return False
    return check_prefix_exactness(seq, small, large)

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    case_count = nums[0]
    cur = 1
    lines = []
    for _ in range(case_count):
        n = nums[cur]
        cur += 1
        seq = nums[cur:cur + n]
        cur += n
        lines.append("VALID" if judge(seq) else "INVALID")
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
