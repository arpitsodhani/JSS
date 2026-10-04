# CLAUSE: setup_environment
import sys
from bisect import bisect_left

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = data[p]
    p += 1
    lines = []
    for _ in range(t):
        n = data[p]
        m = data[p + 1]
        p += 2
        ratings = data[p:p + n]
        p += n
        problems = data[p:p + m]
        p += m
        kevin = ratings[0]
        ratings.sort()
        penalties = []
        for x in problems:
            if x > kevin:
                v = n - bisect_left(ratings, x)
                if v:
                    penalties.append(v)
        penalties.sort(reverse=True)
        h = len(penalties)
        ans = []
        for k in range(1, m + 1):
            total = m // k
            start = min(m % k, h)
            for i in range(start, h, k):
                total += penalties[i]
            ans.append(str(total))
        lines.append(" ".join(ans))
    sys.stdout.write("\n".join(lines))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
