# CLAUSE: setup_environment
import sys

MOD = 10**9 + 7

# CLAUSE: solve_logic
def works_now(a):
    n = len(a)
    for c in range(n):
        if a[c] == -1:
            continue
        lim = min(c + 1, n - c)
        for r in range(1, lim):
            part = a[c - r:c + r + 1]
            if -1 in part:
                continue
            if sorted(part)[r] == a[c]:
                return False
    return True

def count_fillings(n, fixed):
    used = {x for x in fixed if x != -1}
    holes = [i for i, x in enumerate(fixed) if x == -1]
    free = [x for x in range(1, n + 1) if x not in used]
    if len(holes) != len(free):
        return 0
    ans = 0
    a = fixed[:]

    def dfs(k, vals):
        nonlocal ans
        if k == len(holes):
            ans = (ans + 1) % MOD
            return
        p = holes[k]
        for v in vals:
            a[p] = v
            if works_now(a):
                nxt = vals[:]
                nxt.remove(v)
                dfs(k + 1, nxt)
            a[p] = -1

    if works_now(a):
        dfs(0, free)
    return ans

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    at = 1
    out = []
    for _ in range(t):
        n = data[at]
        at += 1
        arr = data[at:at + n]
        at += n
        out.append(str(count_fillings(n, arr)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
