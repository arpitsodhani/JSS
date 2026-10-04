import sys
from collections import Counter

# CLAUSE: split_source_and_target
def split_source_and_target():
    data = sys.stdin.read().splitlines()
    return data[0].strip(), data[1].strip()

# CLAUSE: count_available_letters
def count_available_letters(s):
    return Counter(s)

def consume(counter, ch):
    if counter[ch] == 0:
        return False
    counter[ch] -= 1
    return True

def restore(counter, ch):
    counter[ch] += 1

def ordered_rest(counter):
    parts = []
    for code in range(97, 123):
        ch = chr(code)
        parts.append(ch * counter[ch])
    return ''.join(parts)

# CLAUSE: scan_equal_prefix
def scan_equal_prefix(s, t):
    counter = count_available_letters(s)
    prefix = []
    best = None
    upto = min(len(s), len(t))

    for pos in range(upto):
        target = t[pos]

        # CLAUSE: test_suffix_feasibility
        candidate_letter = ''
        for code in range(ord(target) + 1, ord('z') + 1):
            ch = chr(code)
            if counter[ch]:
                candidate_letter = ch
                break

        # CLAUSE: choose_minimal_exceeding_letter
        if candidate_letter:
            counter[candidate_letter] -= 1
            # CLAUSE: fill_minimal_completion
            best = ''.join(prefix) + candidate_letter + ordered_rest(counter)
            restore(counter, candidate_letter)

        if not consume(counter, target):
            return best

        prefix.append(target)

    if len(s) > len(t) and upto == len(t):
        # CLAUSE: test_suffix_feasibility
        # CLAUSE: choose_minimal_exceeding_letter
        # CLAUSE: fill_minimal_completion
        best = ''.join(prefix) + ordered_rest(counter)

    return best

# CLAUSE: test_suffix_feasibility
# CLAUSE: choose_minimal_exceeding_letter
# CLAUSE: fill_minimal_completion
# CLAUSE: handle_no_solution
def main():
    s, t = split_source_and_target()
    answer = scan_equal_prefix(s, t)
    if answer is None:
        answer = "-1"
    print(answer)

main()
