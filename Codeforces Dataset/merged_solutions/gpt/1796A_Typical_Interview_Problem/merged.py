# Clause generate_reference_window [Confidence: 0.60]
import sys

def make_window(limit):
    chars = []
    number = 1
    while len(chars) < limit:
        chars.extend(emit_for_number(number))
        number += 1
    return "".join(chars)


# Clause encode_divisibility_emissions [Confidence: 0.60]
def encode_divisibility_emissions():
    block = []
    for value in range(1, 16):
        if value % 3 == 0:
            block.append("F")
        if value % 5 == 0:
            block.append("B")
    return "".join(block)


# Clause bound_substring_search_space [Confidence: 0.40]
def bound_substring_search_space(patterns):
    longest = 0
    for pattern in patterns:
        longest = max(longest, len(pattern))
    return longest + 120


# Clause scan_candidate_offsets [Confidence: 0.60]
def scan_candidate_offsets(pattern, reference):
    limit = len(reference) - len(pattern) + 1
    for offset in range(limit):
        if compare_pattern_slice(pattern, reference, offset):
            return True
    return False


# Clause compare_pattern_slice [Confidence: 0.60]
def compare_pattern_slice(pattern, reference, offset):
    return reference[offset:offset + len(pattern)] == pattern


# Clause aggregate_case_verdicts [Confidence: 0.80]
def aggregate_case_verdicts():
    data = sys.stdin.buffer.read().split()
    count = int(data[0])
    strings = [data[2 * i + 2].decode() for i in range(count)]
    reference = generate_reference_window(bound_substring_search_space(strings))
    verdicts = []
    for string in strings:
        verdicts.append("YES" if scan_candidate_offsets(string, reference) else "NO")
    sys.stdout.write("\n".join(verdicts))

aggregate_case_verdicts()


