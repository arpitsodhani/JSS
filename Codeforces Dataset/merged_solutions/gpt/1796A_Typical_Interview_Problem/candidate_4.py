import sys

# CLAUSE: generate_reference_window
def generate_reference_window(required):
    stream = bytearray()
    current = 1
    while len(stream) < required:
        encode_divisibility_emissions(current, stream)
        current += 1
    return bytes(stream)

# CLAUSE: encode_divisibility_emissions
def encode_divisibility_emissions(current, stream):
    if current % 3 == 0:
        stream.append(70)
    if current % 5 == 0:
        stream.append(66)

# CLAUSE: bound_substring_search_space
def bound_substring_search_space(items):
    sizes = [len(item) for item in items]
    if not sizes:
        return 100
    return max(100, max(sizes) + 32)

# CLAUSE: scan_candidate_offsets
def scan_candidate_offsets(pattern, reference):
    pattern = pattern.encode()
    width = len(pattern)
    for offset in range(len(reference) - width + 1):
        if compare_pattern_slice(pattern, reference, offset):
            return True
    return False

# CLAUSE: compare_pattern_slice
def compare_pattern_slice(pattern, reference, offset):
    return reference[offset:offset + len(pattern)] == pattern

# CLAUSE: aggregate_case_verdicts
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
