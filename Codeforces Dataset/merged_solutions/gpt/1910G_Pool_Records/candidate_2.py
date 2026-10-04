import sys
from heapq import heappop, heappush

# CLAUSE: validate_record_order
def validate_record_order(record):
    previous = 0
    for current in record:
        if current <= previous:
            return False
        previous = current
    return bool(record)

# CLAUSE: derive_primary_period
def derive_primary_period(record):
    first = record[0]
    return first

# CLAUSE: classify_primary_multiples
def classify_primary_multiples(record, base):
    explained = []
    for current in record:
        explained.append(current % base == 0)
    return explained

# CLAUSE: infer_secondary_period
def infer_secondary_period(record, explained):
    index = 0
    while index < len(record):
        if not explained[index]:
            return record[index]
        index += 1
    return None

# CLAUSE: merge_two_meeting_sequences
def merge_two_meeting_sequences(base, other, length):
    heap = [(base, base)]
    if other is not None:
        heappush(heap, (other, other))
    merged = []
    last = -1
    while len(merged) < length:
        value, step = heappop(heap)
        if value != last:
            merged.append(value)
            last = value
        heappush(heap, (value + step, step))
    return merged

# CLAUSE: check_prefix_exactness
def check_prefix_exactness(record, base, other):
    generated = merge_two_meeting_sequences(base, other, len(record))
    for got, want in zip(generated, record):
        if got != want:
            return False
    return True

# CLAUSE: handle_degenerate_speed_cases
def handle_degenerate_speed_cases(base, other):
    if other is None:
        return True
    return other > base

def solve_one(record):
    if not validate_record_order(record):
        return False
    base = derive_primary_period(record)
    explained = classify_primary_multiples(record, base)
    other = infer_secondary_period(record, explained)
    if not handle_degenerate_speed_cases(base, other):
        return False
    return check_prefix_exactness(record, base, other)

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    c = values[0]
    at = 1
    output = []
    for _ in range(c):
        n = values[at]
        at += 1
        record = values[at:at + n]
        at += n
        output.append("VALID" if solve_one(record) else "INVALID")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
