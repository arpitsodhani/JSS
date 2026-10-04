# Clause setup_environment [Confidence: 0.60]
import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    out = []


# Clause solve_logic [Confidence: 0.40]
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


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()


