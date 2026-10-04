import sys

# CLAUSE: generate_reference_window
def generate_reference_window(target_size):
    pieces = []
    for number in range(1, target_size * 3 + 20):
        piece = encode_divisibility_emissions(number)
        if piece:
            pieces.append(piece)
            if sum(map(len, pieces)) >= target_size:
                break
    return "".join(pieces)

# CLAUSE: encode_divisibility_emissions
def encode_divisibility_emissions(number):
    text = ""
    if not number % 3:
        text += "F"
    if not number % 5:
        text += "B"
    return text

# CLAUSE: bound_substring_search_space
def bound_substring_search_space(patterns):
    longest = 0
    for pattern in patterns:
        longest = max(longest, len(pattern))
    return longest + 120

# CLAUSE: scan_candidate_offsets
def scan_candidate_offsets(pattern, reference):
    return any(compare_pattern_slice(pattern, reference, start)
               for start in range(0, len(reference) - len(pattern) + 1))

# CLAUSE: compare_pattern_slice
def compare_pattern_slice(pattern, reference, start):
    end = start + len(pattern)
    return reference[start:end] == pattern

# CLAUSE: aggregate_case_verdicts
def aggregate_case_verdicts():
    raw = sys.stdin.read().split()
    t = int(raw[0])
    patterns = [raw[2 * case + 2] for case in range(t)]
    reference = generate_reference_window(bound_substring_search_space(patterns))
    result = []
    for pattern in patterns:
        if scan_candidate_offsets(pattern, reference):
            result.append("YES")
        else:
            result.append("NO")
    print(*result, sep="\n")

aggregate_case_verdicts()
