import sys

# CLAUSE: normalize_run_blocks
def normalize_run_blocks(items):
    res = []
    last_char = None
    for block in items:
        if last_char == block[1]:
            res[-1][0] += block[0]
        else:
            res.append([block[0], block[1]])
            last_char = block[1]
    return res

# CLAUSE: dispatch_pattern_length_case
def dispatch_pattern_length_case(text, pat):
    size = len(pat)
    if size < 2:
        return count_single_block_occurrences(text, pat[0])
    if size == 2:
        return count_two_block_occurrences(text, pat[0], pat[1])
    core = build_middle_pair_pattern(pat)
    places = compute_pair_kmp_matches(text, core)
    return accumulate_occurrence_count(text, pat, places, len(core))

# CLAUSE: count_single_block_occurrences
def count_single_block_occurrences(text, target):
    total = 0
    for block in text:
        extra = block[0] - target[0] + 1
        if block[1] == target[1] and extra > 0:
            total += extra
    return total

# CLAUSE: count_two_block_occurrences
def count_two_block_occurrences(text, left_need, right_need):
    total = 0
    prev = text[0] if text else None
    for cur in text[1:]:
        if prev[1] == left_need[1] and cur[1] == right_need[1] and prev[0] >= left_need[0] and cur[0] >= right_need[0]:
            total += 1
        prev = cur
    return total

# CLAUSE: build_middle_pair_pattern
def build_middle_pair_pattern(pat):
    core = []
    for block in pat[1:len(pat) - 1]:
        core.append((block[0], block[1]))
    return core

# CLAUSE: compute_pair_kmp_matches
def compute_pair_kmp_matches(text, core):
    fail = [0]
    border = 0
    for i in range(1, len(core)):
        while border and core[border] != core[i]:
            border = fail[border - 1]
        if core[border] == core[i]:
            border += 1
        fail.append(border)

    ans = []
    border = 0
    for idx, block in enumerate(text):
        token = (block[0], block[1])
        while border and core[border] != token:
            border = fail[border - 1]
        if core[border] == token:
            border += 1
        if border == len(core):
            ans.append(idx - len(core) + 1)
            border = fail[border - 1]
    return ans

# CLAUSE: validate_boundary_runs
def validate_boundary_runs(text, pat, core_start, core_len):
    left_index = core_start - 1
    right_index = core_start + core_len
    if left_index == -1 or right_index == len(text):
        return False
    left_ok = text[left_index][1] == pat[0][1] and text[left_index][0] >= pat[0][0]
    right_ok = text[right_index][1] == pat[-1][1] and text[right_index][0] >= pat[-1][0]
    return left_ok and right_ok

# CLAUSE: accumulate_occurrence_count
def accumulate_occurrence_count(text, pat, places, core_len):
    total = 0
    for core_start in places:
        if validate_boundary_runs(text, pat, core_start, core_len):
            total += 1
    return total

def parse_block(s):
    a, b = s.split("-", 1)
    return [int(a), b]

def main():
    parts = sys.stdin.read().strip().split()
    n, m = int(parts[0]), int(parts[1])
    text = [parse_block(x) for x in parts[2:2 + n]]
    pat = [parse_block(x) for x in parts[2 + n:2 + n + m]]
    print(dispatch_pattern_length_case(normalize_run_blocks(text), normalize_run_blocks(pat)))

if __name__ == "__main__":
    main()
