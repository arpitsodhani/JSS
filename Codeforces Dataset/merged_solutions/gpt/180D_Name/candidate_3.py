import sys

# CLAUSE: split_source_and_target
def split_source_and_target():
    s, t = sys.stdin.buffer.read().split()
    return s.decode(), t.decode()

# CLAUSE: count_available_letters
def count_available_letters(s):
    bag = {chr(97 + i): 0 for i in range(26)}
    for ch in s:
        bag[ch] += 1
    return bag

def take(bag, ch):
    if bag[ch] == 0:
        return False
    bag[ch] -= 1
    return True

def put(bag, ch):
    bag[ch] += 1

def smallest_tail(bag):
    return ''.join(ch * bag[ch] for ch in map(chr, range(97, 123)))

# CLAUSE: scan_equal_prefix
def solve(s, t):
    bag = count_available_letters(s)
    equal_prefix = []
    best_candidate = None

    for i, target in enumerate(t[:len(s)]):
        # CLAUSE: test_suffix_feasibility
        larger = None
        for code in range(ord(target) + 1, 123):
            ch = chr(code)
            if bag[ch] > 0:
                larger = ch
                break

        # CLAUSE: choose_minimal_exceeding_letter
        if larger is not None:
            bag[larger] -= 1
            # CLAUSE: fill_minimal_completion
            best_candidate = ''.join(equal_prefix) + larger + smallest_tail(bag)
            bag[larger] += 1

        if not take(bag, target):
            break
        equal_prefix.append(target)
    else:
        if len(s) > len(t):
            # CLAUSE: test_suffix_feasibility
            # CLAUSE: choose_minimal_exceeding_letter
            # CLAUSE: fill_minimal_completion
            best_candidate = ''.join(equal_prefix) + smallest_tail(bag)

    return best_candidate

# CLAUSE: test_suffix_feasibility
# CLAUSE: choose_minimal_exceeding_letter
# CLAUSE: fill_minimal_completion
# CLAUSE: handle_no_solution
def main():
    s, t = split_source_and_target()
    result = solve(s, t)
    sys.stdout.write(result if result is not None else "-1")

if __name__ == "__main__":
    main()
