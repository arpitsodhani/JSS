import sys

# CLAUSE: split_source_and_target
def split_source_and_target():
    lines = sys.stdin.read().strip().split()
    s = lines[0]
    t = lines[1]
    return s, t

# CLAUSE: count_available_letters
def count_available_letters(source):
    counts = [0 for _ in range(26)]
    for letter in source:
        counts[ord(letter) - ord('a')] += 1
    return counts

def suffix_from_counts(counts):
    pieces = []
    for idx in range(26):
        pieces.extend(chr(ord('a') + idx) for _ in range(counts[idx]))
    return ''.join(pieces)

# CLAUSE: scan_equal_prefix
def build_answer(s, t):
    counts = count_available_letters(s)
    fixed = []
    answer = None
    n = len(s)
    m = len(t)

    pos = 0
    while pos < n and pos < m:
        target_idx = ord(t[pos]) - ord('a')

        # CLAUSE: test_suffix_feasibility
        chosen = -1
        probe = target_idx + 1
        while probe < 26:
            if counts[probe] > 0:
                chosen = probe
                break
            probe += 1

        # CLAUSE: choose_minimal_exceeding_letter
        if chosen != -1:
            counts[chosen] -= 1
            # CLAUSE: fill_minimal_completion
            answer = ''.join(fixed) + chr(ord('a') + chosen) + suffix_from_counts(counts)
            counts[chosen] += 1

        if counts[target_idx] <= 0:
            return answer

        counts[target_idx] -= 1
        fixed.append(t[pos])
        pos += 1

    if m < n and pos == m:
        # CLAUSE: test_suffix_feasibility
        # CLAUSE: choose_minimal_exceeding_letter
        # CLAUSE: fill_minimal_completion
        answer = ''.join(fixed) + suffix_from_counts(counts)

    return answer

# CLAUSE: test_suffix_feasibility
# CLAUSE: choose_minimal_exceeding_letter
# CLAUSE: fill_minimal_completion
# CLAUSE: handle_no_solution
def handle_no_solution(ans):
    return ans if ans is not None else "-1"

def main():
    s, t = split_source_and_target()
    print(handle_no_solution(build_answer(s, t)))

main()
