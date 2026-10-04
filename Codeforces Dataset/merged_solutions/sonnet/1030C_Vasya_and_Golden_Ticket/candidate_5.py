# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
raw = sys.stdin.read().split()
out = ""
if raw:
    s = raw[0] if len(raw) == 1 else raw[1]
    digits = tuple(map(int, s))
    n = len(digits)
    out = "NO"
    left = 0
    for split_after, digit in enumerate(digits[:-1]):
        left += digit
        segment_sum = 0
        segment_count = 1
        valid = True
        pos = split_after + 1
        while pos < n:
            segment_sum += digits[pos]
            if segment_sum == left:
                segment_count += 1
                segment_sum = 0
            elif segment_sum > left:
                valid = False
                break
            pos += 1
        if valid and segment_sum == 0 and segment_count >= 2:
            out = "YES"
            break

# CLAUSE: finish_program
if out:
    sys.stdout.write(out)
