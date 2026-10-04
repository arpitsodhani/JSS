# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import Counter

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            n = data[idx]
            k = data[idx + 1]
            idx += 2
            a = data[idx:idx + n]
            idx += n

            cnt = Counter(a)
            vals = sorted(cnt)

            best = 0
            cur = 0
            l = 0

            for r, v in enumerate(vals):
                if r > 0 and vals[r] != vals[r - 1] + 1:
                    cur = 0
                    l = r

                cur += cnt[v]

                while r - l + 1 > k:
                    cur -= cnt[vals[l]]
                    l += 1

                if cur > best:
                    best = cur

            ans.append(str(best))

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
