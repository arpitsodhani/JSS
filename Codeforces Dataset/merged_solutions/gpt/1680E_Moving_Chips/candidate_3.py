# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def solve():
        data = sys.stdin.read().strip().split()
        t = int(data[0])
        p = 1
        ans = []

        for _ in range(t):
            n = int(data[p])
            p += 1
            s = data[p]
            p += 1
            r = data[p]
            p += 1

            masks = []
            for i in range(n):
                m = 0
                if s[i] == '*':
                    m |= 1
                if r[i] == '*':
                    m |= 2
                masks.append(m)

            l = 0
            while masks[l] == 0:
                l += 1
            rr = n - 1
            while masks[rr] == 0:
                rr -= 1

            inf = 10 ** 9
            dp = [inf, inf, inf, inf]
            first = masks[l]
            for m in range(1, 4):
                if (m | first) == m:
                    dp[m] = bin(m).count("1") - 1

            for i in range(l + 1, rr + 1):
                need = masks[i]
                ndp = [inf, inf, inf, inf]
                for pm in range(1, 4):
                    if dp[pm] >= inf:
                        continue
                    for cm in range(1, 4):
                        if (cm | need) != cm:
                            continue
                        if pm & cm:
                            cost = bin(cm).count("1")
                        else:
                            cost = bin(cm).count("1") + 1
                        ndp[cm] = min(ndp[cm], dp[pm] + cost)
                dp = ndp

            ans.append(str(min(dp)))

        print("\n".join(ans))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
