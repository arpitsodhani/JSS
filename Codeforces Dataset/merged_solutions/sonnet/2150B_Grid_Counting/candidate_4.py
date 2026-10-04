# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def count_grids(n, a):
    if sum(a) != n:
        return 0

    result = 0
    current = []

    def count_second_permutation(rows):
        memo = {}

        def dfs(i, taken):
            key = (i, taken)
            if key in memo:
                return memo[key]
            if i == n:
                return 1
            k = i + 1
            r = rows[i]
            val = 0
            if r != k:
                q = max(r, n + 1 - k)
                b = 1 << q
                if taken & b == 0:
                    val = dfs(i + 1, taken | b)
            else:
                seen_here = 0
                for c in range(1, k + 1):
                    q = max(k, n + 1 - c)
                    b = 1 << q
                    if taken & b == 0 and seen_here & b == 0:
                        seen_here |= b
                        val += dfs(i + 1, taken | b)
            memo[key] = val % MOD
            return memo[key]

        return dfs(0, 0)

    def build(k, cnt):
        nonlocal result
        if k == n + 1:
            if cnt == a:
                result = (result + count_second_permutation(current)) % MOD
            return
        for row in range(1, k + 1):
            if cnt[row - 1] < a[row - 1]:
                cnt[row - 1] += 1
                current.append(row)
                build(k + 1, cnt)
                current.pop()
                cnt[row - 1] -= 1

    build(1, [0] * n)
    return result

# CLAUSE: finish_program
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
