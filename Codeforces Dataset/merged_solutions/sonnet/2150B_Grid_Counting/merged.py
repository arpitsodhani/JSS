# Clause setup_environment [Confidence: 0.80]
import sys

MOD = 998244353


# Clause solve_logic [Confidence: 0.60]
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


# Clause finish_program [Confidence: 0.60]
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    p = 0
    t = int(data[p])
    p += 1
    res = []
    for _ in range(t):
        n = int(data[p])
        p += 1
        a = []
        for _ in range(n):
            a.append(int(data[p]))
            p += 1
        res.append(str(count_grids(n, a)))
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()


