# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def need(x):
        res = 0
        while x > 0:
            x //= 2
            res += 1
        return res

    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []

    for i in range(1, t + 1):
        s = data[i]
        best = 10**9

        for ch in "abcdefghijklmnopqrstuvwxyz":
            last = -1
            mx = 0
            for j, c in enumerate(s):
                if c == ch:
                    mx = max(mx, j - last - 1)
                    last = j
            mx = max(mx, len(s) - last - 1)
            best = min(best, need(mx))

        ans.append(str(best))

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
