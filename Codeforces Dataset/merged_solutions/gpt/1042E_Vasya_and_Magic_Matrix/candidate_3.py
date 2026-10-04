# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    MOD = 998244353

    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    cells = []
    idx = 2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cells.append((data[idx], i, j))
            idx += 1

    r, c = data[idx], data[idx + 1]

    cells.sort()

    cnt = 0
    sum_i = 0
    sum_j = 0
    sum_i2 = 0
    sum_j2 = 0
    sum_dp = 0

    ans = 0
    p = 0
    total = n * m

    while p < total:
        q = p
        while q < total and cells[q][0] == cells[p][0]:
            q += 1

        group = []
        if cnt:
            inv = pow(cnt, MOD - 2, MOD)
            for k in range(p, q):
                val, i, j = cells[k]
                dp = (
                    sum_dp
                    + cnt * (i * i + j * j)
                    - 2 * i * sum_i
                    - 2 * j * sum_j
                    + sum_i2
                    + sum_j2
                ) % MOD
                dp = dp * inv % MOD
                group.append((i, j, dp))
                if i == r and j == c:
                    ans = dp
        else:
            for k in range(p, q):
                val, i, j = cells[k]
                group.append((i, j, 0))
                if i == r and j == c:
                    ans = 0

        for i, j, dp in group:
            cnt += 1
            sum_i = (sum_i + i) % MOD
            sum_j = (sum_j + j) % MOD
            sum_i2 = (sum_i2 + i * i) % MOD
            sum_j2 = (sum_j2 + j * j) % MOD
            sum_dp = (sum_dp + dp) % MOD

        p = q

    print(ans % MOD)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
