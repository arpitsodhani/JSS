# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().split()
    t = int(data[0])
    ans = []
    p = 1

    for _ in range(t):
        n = int(data[p])
        s = data[p + 1]
        p += 2

        left = s[:n]
        right = s[n:]

        wl = left.count('W')
        rr = right.count('R')

        if wl % 2 or rr % 2:
            ans.append("NO")
            continue

        pref_w = 0
        for c in left:
            if c == 'W':
                pref_w += 1
            else:
                break

        suff_r = 0
        for c in reversed(right):
            if c == 'R':
                suff_r += 1
            else:
                break

        if pref_w >= wl // 2 and suff_r >= rr // 2:
            ans.append("YES")
        else:
            ans.append("NO")

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
