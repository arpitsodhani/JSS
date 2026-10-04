import sys

# CLAUSE: generate_reference_window
def generate_reference_window(limit):
    cycle = encode_divisibility_emissions()
    reference = []
    while len("".join(reference)) < limit:
        reference.append(cycle)
    return "".join(reference)

# CLAUSE: encode_divisibility_emissions
def encode_divisibility_emissions():
    emitted = []
    for number in (3, 5, 6, 9, 10, 12, 15):
        if number % 3 == 0:
            emitted.append("F")
        if number % 5 == 0:
            emitted.append("B")
    return "".join(emitted)

# CLAUSE: bound_substring_search_space
def bound_substring_search_space(patterns):
    longest = max([0] + [len(pattern) for pattern in patterns])
    period_length = len(encode_divisibility_emissions())
    return ((longest + period_length * 3 + 99) // period_length) * period_length

# CLAUSE: scan_candidate_offsets
def scan_candidate_offsets(pattern, reference):
    limit = len(reference) - len(pattern) + 1
    for offset in range(limit):
        if compare_pattern_slice(pattern, reference, offset):
            return True
    return False

# CLAUSE: compare_pattern_slice
def compare_pattern_slice(pattern, reference, offset):
    index = 0
    while index < len(pattern):
        if pattern[index] != reference[offset + index]:
            return False
        index += 1
    return True

# CLAUSE: aggregate_case_verdicts
def aggregate_case_verdicts():
    tokens = sys.stdin.read().strip().split()
    t = int(tokens[0])
    patterns = []
    cursor = 1
    for _ in range(t):
        cursor += 1
        patterns.append(tokens[cursor])
        cursor += 1
    reference = generate_reference_window(bound_substring_search_space(patterns))
    sys.stdout.write("\n".join(["YES" if scan_candidate_offsets(p, reference) else "NO" for p in patterns]))

aggregate_case_verdicts()
