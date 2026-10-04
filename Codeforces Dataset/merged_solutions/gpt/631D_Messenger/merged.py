import sys

# CLAUSE: normalize_run_blocks
def normalize_run_blocks(blocks):
    out = []
    for length, ch in blocks:
        if out and out[-1][1] == ch:
            out[-1] = (out[-1][0] + length, ch)
        else:
            out.append((length, ch))
    return out

# CLAUSE: dispatch_pattern_length_case
def solve(text, pattern):
    k = len(pattern)
    if k == 1:
        return count_single_block_occurrences(text, pattern[0])
    if k == 2:
        return count_two_block_occurrences(text, pattern)
    middle = build_middle_pair_pattern(pattern)
    matches = compute_pair_kmp_matches(text, middle)
    return accumulate_occurrence_count(text, pattern, matches, len(middle))

# CLAUSE: count_single_block_occurrences
def count_single_block_occurrences(text, one):
    need_len, need_ch = one
    total = 0
    for length, ch in text:
        if ch == need_ch and length >= need_len:
            total += length - need_len + 1
    return total

# CLAUSE: count_two_block_occurrences
def count_two_block_occurrences(text, pattern):
    first, second = pattern
    total = 0
    for i in range(len(text) - 1):
        a = text[i]
        b = text[i + 1]
        if a[1] == first[1] and b[1] == second[1] and a[0] >= first[0] and b[0] >= second[0]:
            total += 1
    return total

# CLAUSE: build_middle_pair_pattern
def build_middle_pair_pattern(pattern):
    return pattern[1:-1]

# CLAUSE: compute_pair_kmp_matches
def compute_pair_kmp_matches(text, middle):
    pref = [0] * len(middle)
    j = 0
    for i in range(1, len(middle)):
        while j and middle[i] != middle[j]:
            j = pref[j - 1]
        if middle[i] == middle[j]:
            j += 1
        pref[i] = j

    starts = []
    j = 0
    for i, item in enumerate(text):
        while j and item != middle[j]:
            j = pref[j - 1]
        if item == middle[j]:
            j += 1
        if j == len(middle):
            starts.append(i - len(middle) + 1)
            j = pref[j - 1]
    return starts

# CLAUSE: validate_boundary_runs
def validate_boundary_runs(text, pattern, start, middle_len):
    left = start - 1
    right = start + middle_len
    if left < 0 or right >= len(text):
        return False
    first = pattern[0]
    last = pattern[-1]
    return text[left][1] == first[1] and text[left][0] >= first[0] and text[right][1] == last[1] and text[right][0] >= last[0]

# CLAUSE: accumulate_occurrence_count
def accumulate_occurrence_count(text, pattern, matches, middle_len):
    ans = 0
    for start in matches:
        if validate_boundary_runs(text, pattern, start, middle_len):
            ans += 1
    return ans

def read_blocks(tokens, pos, count):
    blocks = []
    for _ in range(count):
        raw = tokens[pos]
        pos += 1
        length, ch = raw.split("-")
        blocks.append((int(length), ch))
    return blocks, pos

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    text, pos = read_blocks(data, 2, n)
    pattern, pos = read_blocks(data, pos, m)
    print(solve(normalize_run_blocks(text), normalize_run_blocks(pattern)))

if __name__ == "__main__":
    main()
