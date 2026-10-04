import sys

# CLAUSE: normalize_run_blocks
def normalize_run_blocks(seq):
    normalized = []
    for length, letter in seq:
        if normalized and normalized[-1][0] == letter:
            normalized[-1][1] += length
        else:
            normalized.append([letter, length])
    return normalized

# CLAUSE: dispatch_pattern_length_case
def dispatch_pattern_length_case(text, pattern):
    run_count = len(pattern)
    if run_count == 1:
        return count_single_block_occurrences(text, pattern[0])
    if run_count == 2:
        return count_two_block_occurrences(text, pattern)
    wanted = build_middle_pair_pattern(pattern)
    hits = compute_pair_kmp_matches(text, wanted)
    return accumulate_occurrence_count(text, pattern, hits, len(wanted))

# CLAUSE: count_single_block_occurrences
def count_single_block_occurrences(text, pattern_block):
    ch, amount = pattern_block
    answer = 0
    for t_ch, t_amount in text:
        if t_ch == ch and t_amount >= amount:
            answer += t_amount - amount + 1
    return answer

# CLAUSE: count_two_block_occurrences
def count_two_block_occurrences(text, pattern):
    answer = 0
    first_ch, first_len = pattern[0]
    second_ch, second_len = pattern[1]
    for left, right in zip(text, text[1:]):
        if left[0] == first_ch and right[0] == second_ch and left[1] >= first_len and right[1] >= second_len:
            answer += 1
    return answer

# CLAUSE: build_middle_pair_pattern
def build_middle_pair_pattern(pattern):
    return [(block[0], block[1]) for block in pattern[1:-1]]

# CLAUSE: compute_pair_kmp_matches
def compute_pair_kmp_matches(text, wanted):
    prefix = [0] * (len(wanted) + 1)
    for i in range(1, len(wanted)):
        j = prefix[i]
        while j and wanted[i] != wanted[j]:
            j = prefix[j]
        if wanted[i] == wanted[j]:
            j += 1
        prefix[i + 1] = j

    matches = []
    j = 0
    for i in range(len(text)):
        item = (text[i][0], text[i][1])
        while j and item != wanted[j]:
            j = prefix[j]
        if item == wanted[j]:
            j += 1
        if j == len(wanted):
            matches.append(i - len(wanted) + 1)
            j = prefix[j]
    return matches

# CLAUSE: validate_boundary_runs
def validate_boundary_runs(text, pattern, start, span):
    before = start - 1
    after = start + span
    if before < 0 or after >= len(text):
        return False
    return (
        text[before][0] == pattern[0][0]
        and text[before][1] >= pattern[0][1]
        and text[after][0] == pattern[-1][0]
        and text[after][1] >= pattern[-1][1]
    )

# CLAUSE: accumulate_occurrence_count
def accumulate_occurrence_count(text, pattern, hits, span):
    return sum(1 for start in hits if validate_boundary_runs(text, pattern, start, span))

def parse_many(raw, start, total):
    seq = []
    for i in range(start, start + total):
        length, letter = raw[i].split("-")
        seq.append((int(length), letter))
    return seq

def main():
    raw = sys.stdin.readline().split()
    while len(raw) < 2:
        raw += sys.stdin.readline().split()
    n = int(raw[0])
    m = int(raw[1])
    rest = sys.stdin.read().split()
    raw += rest
    text = parse_many(raw, 2, n)
    pattern = parse_many(raw, 2 + n, m)
    text = normalize_run_blocks(text)
    pattern = normalize_run_blocks(pattern)
    sys.stdout.write(str(dispatch_pattern_length_case(text, pattern)))

if __name__ == "__main__":
    main()
