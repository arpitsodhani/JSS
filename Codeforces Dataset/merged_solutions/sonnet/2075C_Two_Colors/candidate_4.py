# CLAUSE: setup_environment
import sys
from bisect import bisect_left

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    tc = nums[at]
    at += 1
    res = []

# CLAUSE: solve_logic
    for _ in range(tc):
        n = nums[at]
        m = nums[at + 1]
        at += 2
        caps = [min(x, n - 1) for x in nums[at:at + m]]
        at += m
        caps.sort()
        pref = [0]
        for x in caps:
            pref.append(pref[-1] + x)
        total = 0
        for x in caps:
            need = n - x
            j = bisect_left(caps, need)
            count = m - j
            total += pref[m] - pref[j] + count * (x - n + 1)
            if x + x >= n:
                total -= x + x - n + 1
        res.append(str(total))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
