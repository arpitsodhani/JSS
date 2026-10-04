import sys

# CLAUSE: split_source_and_target
def split_source_and_target():
    data = sys.stdin.read().split()
    return data[0], data[1]

# CLAUSE: count_available_letters
def count_available_letters(s):
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - 97] += 1
    return freq

def expand(freq):
    out = []
    for i, v in enumerate(freq):
        if v:
            out.append(chr(97 + i) * v)
    return ''.join(out)

# CLAUSE: scan_equal_prefix
def scan_equal_prefix(s, t):
    freq = count_available_letters(s)
    prefix = []
    best = None
    limit = min(len(s), len(t))

    for i in range(limit):
        c = ord(t[i]) - 97

        # CLAUSE: test_suffix_feasibility
        bigger = None
        for j in range(c + 1, 26):
            if freq[j]:
                bigger = j
                break

        if bigger is not None:
            # CLAUSE: choose_minimal_exceeding_letter
            freq[bigger] -= 1
            # CLAUSE: fill_minimal_completion
            best = ''.join(prefix) + chr(97 + bigger) + expand(freq)
            freq[bigger] += 1

        if freq[c] == 0:
            break
        freq[c] -= 1
        prefix.append(t[i])
    else:
        if len(s) > len(t):
            # CLAUSE: test_suffix_feasibility
            # CLAUSE: choose_minimal_exceeding_letter
            # CLAUSE: fill_minimal_completion
            best = ''.join(prefix) + expand(freq)

    return best

# CLAUSE: test_suffix_feasibility
# CLAUSE: choose_minimal_exceeding_letter
# CLAUSE: fill_minimal_completion
# CLAUSE: handle_no_solution
def main():
    s, t = split_source_and_target()
    ans = scan_equal_prefix(s, t)
    print(ans if ans is not None else -1)

if __name__ == "__main__":
    main()
