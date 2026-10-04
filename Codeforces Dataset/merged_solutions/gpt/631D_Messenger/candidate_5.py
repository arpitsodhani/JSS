import sys

# CLAUSE: normalize_run_blocks
def normalize_run_blocks(blocks):
    ans = []
    for block in blocks:
        length = block[0]
        char = block[1]
        if len(ans) != 0 and ans[-1][1] == char:
            old_length, old_char = ans.pop()
            ans.append((old_length + length, old_char))
        else:
            ans.append(block)
    return ans

# CLAUSE: dispatch_pattern_length_case
def dispatch_pattern_length_case(text, pattern):
    handlers = {
        1: lambda: count_single_block_occurrences(text, pattern[0]),
        2: lambda: count_two_block_occurrences(text, pattern),
    }
    if len(pattern) in handlers:
        return handlers[len(pattern)]()
    middle = build_middle_pair_pattern(pattern)
    matched_at = compute_pair_kmp_matches(text, middle)
    return accumulate_occurrence_count(text, pattern, matched_at, len(middle))

# CLAUSE: count_single_block_occurrences
def count_single_block_occurrences(text, block):
    need_length, need_char = block
    total = 0
    for length, char in text:
        if char != need_char:
            continue
        if length >= need_length:
            total += length - need_length + 1
    return total

# CLAUSE: count_two_block_occurrences
def count_two_block_occurrences(text, pattern):
    total = 0
    a_len, a_char = pattern[0]
    b_len, b_char = pattern[1]
    i = 0
    while i + 1 < len(text):
        left_len, left_char = text[i]
        right_len, right_char = text[i + 1]
        if left_char == a_char and right_char == b_char and left_len >= a_len and right_len >= b_len:
            total += 1
        i += 1
    return total

# CLAUSE: build_middle_pair_pattern
def build_middle_pair_pattern(pattern):
    middle = pattern[:]
    del middle[0]
    del middle[-1]
    return middle

# CLAUSE: compute_pair_kmp_matches
def compute_pair_kmp_matches(text, middle):
    link = [0 for _ in middle]
    pos = 1
    matched = 0
    while pos < len(middle):
        if middle[pos] == middle[matched]:
            matched += 1
            link[pos] = matched
            pos += 1
        elif matched:
            matched = link[matched - 1]
        else:
            link[pos] = 0
            pos += 1

    starts = []
    ti = 0
    pi = 0
    while ti < len(text):
        if text[ti] == middle[pi]:
            ti += 1
            pi += 1
            if pi == len(middle):
                starts.append(ti - pi)
                pi = link[pi - 1]
        elif pi:
            pi = link[pi - 1]
        else:
            ti += 1
    return starts

# CLAUSE: validate_boundary_runs
def validate_boundary_runs(text, pattern, start, middle_len):
    if start <= 0:
        return False
    if start + middle_len >= len(text):
        return False
    left_len, left_char = text[start - 1]
    right_len, right_char = text[start + middle_len]
    first_len, first_char = pattern[0]
    last_len, last_char = pattern[-1]
    return left_char == first_char and right_char == last_char and left_len >= first_len and right_len >= last_len

# CLAUSE: accumulate_occurrence_count
def accumulate_occurrence_count(text, pattern, matched_at, middle_len):
    total = 0
    for start in matched_at:
        total += int(validate_boundary_runs(text, pattern, start, middle_len))
    return total

def read_input():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    m = int(raw[1])
    blocks = []
    for token in raw[2:]:
        length, char = token.split(b"-")
        blocks.append((int(length), char.decode()))
    return blocks[:n], blocks[n:n + m]

def main():
    text, pattern = read_input()
    text = normalize_run_blocks(text)
    pattern = normalize_run_blocks(pattern)
    print(dispatch_pattern_length_case(text, pattern))

if __name__ == "__main__":
    main()
