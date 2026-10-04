# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def next_visit(after_day, start, period):
    if start > after_day:
        return start
    return start + ((after_day - start) // period + 1) * period

def main():
    nums = [int(x) for x in sys.stdin.buffer.read().split()]
    pairs = zip(nums[1::2], nums[2::2])
    current = 0
    for start, period in pairs:
        current = next_visit(current, start, period)
    sys.stdout.write(str(current))

# CLAUSE: finish_program
main()
