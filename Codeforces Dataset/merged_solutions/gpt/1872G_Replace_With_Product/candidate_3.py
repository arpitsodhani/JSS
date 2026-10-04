# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        ans = []
        INF = 10 ** 30

        for _ in range(t):
            n = data[idx]
            idx += 1
            a = data[idx:idx + n]
            idx += n

            pos = [i for i, x in enumerate(a) if x > 1]

            if not pos:
                ans.append("1 1")
                continue

            pref = [0]
            for x in a:
                pref.append(pref[-1] + x)

            m = len(pos)
            best = 0
            best_l = best_r = 0

            for i in range(m):
                prod = 1
                for j in range(i, m):
                    prod *= a[pos[j]]
                    if prod > INF:
                        prod = INF
                    s = pref[pos[j] + 1] - pref[pos[i]]
                    cur = prod - s
                    if cur > best:
                        best = cur
                        best_l = pos[i]
                        best_r = pos[j]
                    if prod == INF:
                        break

            ans.append(f"{best_l + 1} {best_r + 1}")

        print("\n".join(ans))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
