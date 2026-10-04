# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    intervals = []
    p = 1
    for i in range(1, n + 1):
        l = data[p]
        r = data[p + 1]
        p += 2
        intervals.append((l, r, i))

    intervals.sort()

    if n == 1:
        print(1)
        print(intervals[0][2])
        return

    bad = [0] * (n - 1)
    total_bad = 0
    for i in range(n - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            bad[i] = 1
            total_bad += 1

    ans = []
    for i in range(n):
        removed_bad = 0
        if i > 0:
            removed_bad += bad[i - 1]
        if i < n - 1:
            removed_bad += bad[i]

        if total_bad - removed_bad != 0:
            continue

        if 0 < i < n - 1 and intervals[i - 1][1] > intervals[i + 1][0]:
            continue

        ans.append(intervals[i][2])

    ans.sort()
    print(len(ans))
    if ans:
        print(*ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
