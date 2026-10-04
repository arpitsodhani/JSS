import sys

# CLAUSE: generate_reference_window
def generate_reference_window(length):
    period = encode_divisibility_emissions()
    copies = length // len(period) + 3
    return (period * copies)[:length]

# CLAUSE: encode_divisibility_emissions
def encode_divisibility_emissions():
    block = []
    for value in range(1, 16):
        if value % 3 == 0:
            block.append("F")
        if value % 5 == 0:
            block.append("B")
    return "".join(block)

# CLAUSE: bound_substring_search_space
def bound_substring_search_space(strings):
    max_len = 0
    for text in strings:
        if len(text) > max_len:
            max_len = len(text)
    return max(96, max_len + len(encode_divisibility_emissions()) * 3)

# CLAUSE: scan_candidate_offsets
def scan_candidate_offsets(pattern, reference):
    last = len(reference) - len(pattern)
    offset = 0
    while offset <= last:
        if compare_pattern_slice(pattern, reference, offset):
            return True
        offset += 1
    return False

# CLAUSE: compare_pattern_slice
def compare_pattern_slice(pattern, reference, offset):
    for index, char in enumerate(pattern):
        if reference[offset + index] != char:
            return False
    return True

# CLAUSE: aggregate_case_verdicts
def aggregate_case_verdicts():
    tokens = sys.stdin.read().split()
    total = int(tokens[0])
    queries = []
    position = 1
    for _ in range(total):
        position += 1
        queries.append(tokens[position])
        position += 1
    reference = generate_reference_window(bound_substring_search_space(queries))
    answers = []
    for query in queries:
        answers.append("YES" if scan_candidate_offsets(query, reference) else "NO")
    sys.stdout.write("\n".join(answers))

aggregate_case_verdicts()
