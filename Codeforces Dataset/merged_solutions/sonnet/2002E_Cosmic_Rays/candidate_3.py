# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def shrink(values, lengths):
    while len(values) >= 2:
        last = len(values) - 1
        if values[last] == values[last - 1]:
            lengths[last - 1] += lengths[last]
            values.pop()
            lengths.pop()
            continue
        if len(values) >= 3 and values[last] == values[last - 2]:
            middle = lengths[last - 1]
            left = lengths[last - 2]
            right = lengths[last]
            if middle < left and middle < right:
                kept = values[last]
                merged = left + right - middle
                values.pop()
                values.pop()
                values.pop()
                lengths.pop()
                lengths.pop()
                lengths.pop()
                values.append(kept)
                lengths.append(merged)
                continue
        break

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    t = nums[at]
    at += 1
    lines = []
    for _ in range(t):
        n = nums[at]
        at += 1
        vals = []
        lens = []
        peak = 0
        cur = []
        for _ in range(n):
            lens.append(nums[at])
            vals.append(nums[at + 1])
            at += 2
            shrink(vals, lens)
            if lens[-1] > peak:
                peak = lens[-1]
            cur.append(str(peak))
        lines.append(" ".join(cur))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
main()
