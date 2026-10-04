import sys

# CLAUSE: generate_reference_window
def make_window(limit):
    chars = []
    number = 1
    while len(chars) < limit:
        chars.extend(emit_for_number(number))
        number += 1
    return "".join(chars)

# CLAUSE: encode_divisibility_emissions
def emit_for_number(number):
    out = []
    if number % 3 == 0:
        out.append("F")
    if number % 5 == 0:
        out.append("B")
    return out

# CLAUSE: bound_substring_search_space
def needed_length(cases):
    longest = max((len(s) for s in cases), default=0)
    return max(100, longest + 20)

# CLAUSE: scan_candidate_offsets
def exists_in_window(pattern, window):
    for start in range(len(window) - len(pattern) + 1):
        if compare_slice(pattern, window, start):
            return True
    return False

# CLAUSE: compare_pattern_slice
def compare_slice(pattern, window, start):
    return window[start:start + len(pattern)] == pattern

# CLAUSE: aggregate_case_verdicts
def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    cases = [data[i] for i in range(2, 2 * t + 1, 2)]
    window = make_window(needed_length(cases))
    print("\n".join("YES" if exists_in_window(s, window) else "NO" for s in cases))

if __name__ == "__main__":
    main()
