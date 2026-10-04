# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def solve_case(n, a):
    if sum(a) != n:
        return 0

    ans = 0
    rows = [0] * (n + 1)
    used = [False] * (n + 1)

    def put_columns(k):
        if k > n:
            return 1
        r = rows[k]
        if r < k:
            q = max(r, n + 1 - k)
            if used[q]:
                return 0
            used[q] = True
            got = put_columns(k + 1)
            used[q] = False
            return got
        total = 0
        for c in range(1, k + 1):
            q = max(k, n + 1 - c)
            if not used[q]:
                used[q] = True
                total += put_columns(k + 1)
                used[q] = False
        return total % MOD

    def choose_rows(k, left):
        nonlocal ans
        if k == n + 1:
            if all(x == 0 for x in left):
                ans = (ans + put_columns(1)) % MOD
            return
        for r in range(1, k + 1):
            if left[r - 1]:
                left[r - 1] -= 1
                rows[k] = r
                choose_rows(k + 1, left)
                left[r - 1] += 1

    choose_rows(1, a[:])
    return ans

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    t = data[0]
    pos = 1
    out = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        arr = data[pos:pos + n]
        pos += n
        out.append(str(solve_case(n, arr)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
