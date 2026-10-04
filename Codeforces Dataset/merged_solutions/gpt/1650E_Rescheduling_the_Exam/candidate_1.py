# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve_case(n, d, a):
    a.sort()
    g = [a[0] - 1]
    for i in range(1, n):
        g.append(a[i] - a[i - 1] - 1)

    def can(k):
        pref_bad = [0] * (n + 1)
        pref_max = [-1] * (n + 1)
        for i in range(n):
            pref_bad[i + 1] = pref_bad[i] + (g[i] < k)
            pref_max[i + 1] = max(pref_max[i], g[i])

        suf_bad = [0] * (n + 1)
        suf_max = [-1] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_bad[i] = suf_bad[i + 1] + (g[i] < k)
            suf_max[i] = max(suf_max[i + 1], g[i])

        for j in range(n):
            if j < n - 1:
                if pref_bad[j] + suf_bad[j + 2]:
                    continue
                prev = 0 if j == 0 else a[j - 1]
                merged = a[j + 1] - prev - 1
                if merged < k:
                    continue
                best_gap = max(pref_max[j], suf_max[j + 2], merged)
            else:
                if pref_bad[j]:
                    continue
                best_gap = pref_max[j]

            if j == n - 1:
                last = 0 if n == 1 else a[n - 2]
            else:
                last = a[-1]

            if best_gap >= 2 * k + 1 or d - last >= k + 1:
                return True

        return False

    lo, hi = 0, d - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if can(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        d = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n
        ans.append(str(solve_case(n, d, a)))
    print("\n".join(ans))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
