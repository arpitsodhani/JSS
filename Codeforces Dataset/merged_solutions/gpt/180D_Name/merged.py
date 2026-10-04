# Clause program [Confidence: 1.00]
import sys

# CLAUSE: split_source_and_target
def split_source_and_target():
    tokens = sys.stdin.readline().strip(), sys.stdin.readline().strip()
    return tokens

# CLAUSE: count_available_letters
def count_available_letters(s):
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - 97] += 1
    return freq

def make_sorted(freq):
    return ''.join(chr(97 + i) * freq[i] for i in range(26))

# CLAUSE: scan_equal_prefix
def scan_equal_prefix(s, t):
    n = len(s)
    m = len(t)
    freq = count_available_letters(s)
    prefix_chars = []
    last_good = None

    for pos in range(min(n, m)):
        target = ord(t[pos]) - 97

        # CLAUSE: test_suffix_feasibility
        options = [i for i in range(target + 1, 26) if freq[i] > 0]
        if options:
            # CLAUSE: choose_minimal_exceeding_letter
            pick = options[0]
            freq[pick] -= 1
            # CLAUSE: fill_minimal_completion
            last_good = ''.join(prefix_chars) + chr(97 + pick) + make_sorted(freq)
            freq[pick] += 1

        if freq[target] < 1:
            return last_good

        freq[target] -= 1
        prefix_chars.append(t[pos])

    if n > m and len(prefix_chars) == m:
        # CLAUSE: test_suffix_feasibility
        # CLAUSE: choose_minimal_exceeding_letter
        # CLAUSE: fill_minimal_completion
        last_good = ''.join(prefix_chars) + make_sorted(freq)

    return last_good

# CLAUSE: test_suffix_feasibility
# CLAUSE: choose_minimal_exceeding_letter
# CLAUSE: fill_minimal_completion
# CLAUSE: handle_no_solution
def handle_no_solution(value):
    if value is None:
        print(-1)
    else:
        print(value)

def main():
    s, t = split_source_and_target()
    handle_no_solution(scan_equal_prefix(s, t))

if __name__ == "__main__":
    main()


