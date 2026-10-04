# CLAUSE: setup_environment
import sys
from bisect import bisect_left

def tri(a):
    return a * (a + 1) // 2

def last_days(month_len, take):
    return tri(month_len) - tri(month_len - take)

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    x = values[1]
    months = values[2:] * 2

    day_prefix = [0]
    hug_prefix = [0]
    for days in months:
        day_prefix.append(day_prefix[-1] + days)
        hug_prefix.append(hug_prefix[-1] + tri(days))

    ans = 0
    for end in range(n, 2 * n + 1):
        target = day_prefix[end] - x
        start = bisect_left(day_prefix, target, 0, end + 1)
        got = hug_prefix[end] - hug_prefix[start]
        extra = day_prefix[start] - target
        if extra and start:
            got += last_days(months[start - 1], extra)
        if got > ans:
            ans = got

    sys.stdout.write(str(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
