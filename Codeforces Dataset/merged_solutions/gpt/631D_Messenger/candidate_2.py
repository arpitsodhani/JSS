import sys

# CLAUSE: normalize_run_blocks
def normalize_run_blocks(lengths, chars):
    nl = []
    nc = []
    for length, ch in zip(lengths, chars):
        if nc and nc[-1] == ch:
            nl[-1] += length
        else:
            nl.append(length)
            nc.append(ch)
    return nl, nc

# CLAUSE: dispatch_pattern_length_case
def dispatch_pattern_length_case(tl, tc, pl, pc):
    if len(pl) == 1:
        return count_single_block_occurrences(tl, tc, pl[0], pc[0])
    if len(pl) == 2:
        return count_two_block_occurrences(tl, tc, pl, pc)
    middle = build_middle_pair_pattern(pl, pc)
    starts = compute_pair_kmp_matches(tl, tc, middle)
    return accumulate_occurrence_count(tl, tc, pl, pc, starts, len(middle))

# CLAUSE: count_single_block_occurrences
def count_single_block_occurrences(tl, tc, need_len, need_ch):
    ans = 0
    for i in range(len(tl)):
        if tc[i] == need_ch and tl[i] >= need_len:
            ans += tl[i] - need_len + 1
    return ans

# CLAUSE: count_two_block_occurrences
def count_two_block_occurrences(tl, tc, pl, pc):
    ans = 0
    for i in range(len(tl) - 1):
        if tc[i] == pc[0] and tc[i + 1] == pc[1] and tl[i] >= pl[0] and tl[i + 1] >= pl[1]:
            ans += 1
    return ans

# CLAUSE: build_middle_pair_pattern
def build_middle_pair_pattern(pl, pc):
    return list(zip(pl[1:-1], pc[1:-1]))

# CLAUSE: compute_pair_kmp_matches
def compute_pair_kmp_matches(tl, tc, pat):
    pi = [0] * len(pat)
    for i in range(1, len(pat)):
        k = pi[i - 1]
        while k > 0 and pat[i] != pat[k]:
            k = pi[k - 1]
        if pat[i] == pat[k]:
            k += 1
        pi[i] = k

    found = []
    k = 0
    for i in range(len(tl)):
        cur = (tl[i], tc[i])
        while k > 0 and cur != pat[k]:
            k = pi[k - 1]
        if cur == pat[k]:
            k += 1
        if k == len(pat):
            found.append(i + 1 - len(pat))
            k = pi[k - 1]
    return found

# CLAUSE: validate_boundary_runs
def validate_boundary_runs(tl, tc, pl, pc, start, middle_len):
    lpos = start - 1
    rpos = start + middle_len
    return lpos >= 0 and rpos < len(tl) and tc[lpos] == pc[0] and tl[lpos] >= pl[0] and tc[rpos] == pc[-1] and tl[rpos] >= pl[-1]

# CLAUSE: accumulate_occurrence_count
def accumulate_occurrence_count(tl, tc, pl, pc, starts, middle_len):
    total = 0
    for start in starts:
        total += 1 if validate_boundary_runs(tl, tc, pl, pc, start, middle_len) else 0
    return total

def parse(data, at, count):
    lengths = []
    chars = []
    for _ in range(count):
        x = data[at]
        at += 1
        p = x.index("-")
        lengths.append(int(x[:p]))
        chars.append(x[p + 1:])
    return lengths, chars, at

def main():
    data = sys.stdin.buffer.read().decode().split()
    n = int(data[0])
    m = int(data[1])
    tl, tc, at = parse(data, 2, n)
    pl, pc, at = parse(data, at, m)
    tl, tc = normalize_run_blocks(tl, tc)
    pl, pc = normalize_run_blocks(pl, pc)
    print(dispatch_pattern_length_case(tl, tc, pl, pc))

main()
