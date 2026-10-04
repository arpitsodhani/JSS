# CLAUSE: setup_environment
import sys

def tri(k):
    return k * (k + 1) // 2

def suffix_value(days, amount):
    return (days - amount + 1 + days) * amount // 2

# CLAUSE: solve_logic
def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n, x = raw[0], raw[1]
    calendar = raw[2:] + raw[2:]

    best = 0
    left = 0
    days_in_window = 0
    hugs_in_window = 0

    for right, length in enumerate(calendar):
        days_in_window += length
        hugs_in_window += tri(length)

        while left <= right and days_in_window - calendar[left] >= x:
            days_in_window -= calendar[left]
            hugs_in_window -= tri(calendar[left])
            left += 1

        excess = days_in_window - x
        candidate = hugs_in_window
        if excess > 0:
            candidate -= excess * (excess + 1) // 2

        if days_in_window >= x and candidate > best:
            best = candidate

    print(best)

# CLAUSE: finish_program
main()
