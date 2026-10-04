# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from collections import Counter

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        cnt = Counter(a)
        days = sorted(cnt)

        best = 0
        dp0 = 0
        dp1 = 0
        prev = -10

        for x in days:
            c = cnt[x]

            if x == prev + 1:
                ndp0 = dp1 + 1
                ndp1 = dp0 + 1 if c >= 2 else 0
            elif x == prev + 2:
                ndp0 = 1
                ndp1 = dp1 + 1
            else:
                ndp0 = 1
                ndp1 = 2 if c >= 2 else 1

            dp0, dp1 = ndp0, ndp1
            best = max(best, dp0, dp1)
            prev = x

        ans.append(str(best))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
