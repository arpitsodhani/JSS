# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def answer(n, a):
    if sum(a) != n:
        return 0

    def column_options(k, r):
        if r < k:
            return (max(r, n + 1 - k),)
        vals = []
        last = 0
        for c in range(1, k + 1):
            q = max(k, n + 1 - c)
            if q != last:
                vals.append(q)
                last = q
        return tuple(vals)

    ans = 0
    assignment = [0] * n
    remaining = a[:]

    def columns(pos, used):
        if pos == n:
            return 1
        s = 0
        for q in column_options(pos + 1, assignment[pos]):
            bit = 1 << q
            if used & bit == 0:
                s += columns(pos + 1, used | bit)
        return s % MOD

    def rows(pos):
        nonlocal ans
        if pos == n:
            ans = (ans + columns(0, 0)) % MOD
            return
        k = pos + 1
        for r in range(1, k + 1):
            if remaining[r - 1] > 0:
                remaining[r - 1] -= 1
                assignment[pos] = r
                rows(pos + 1)
                remaining[r - 1] += 1

    rows(0)
    return ans

# CLAUSE: finish_program
def main():
    it = iter(sys.stdin.buffer.read().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        out.append(str(answer(n, a)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
