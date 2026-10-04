# CLAUSE: setup_environment
import sys
from functools import lru_cache

# CLAUSE: solve_logic
MOD = 998244353

l, r, k = map(int, sys.stdin.readline().split())

def solve(n):
    if n <= 0:
        return 0

    digits = list(map(int, str(n)))
    m = len(digits)
    pow10 = [1] * (m + 1)
    for i in range(1, m + 1):
        pow10[i] = pow10[i - 1] * 10 % MOD

    @lru_cache(None)
    def dp(pos, mask, tight, started):
        if pos == m:
            return 1, 0

        limit = digits[pos] if tight else 9
        rem = m - pos - 1
        total_count = 0
        total_sum = 0

        for d in range(limit + 1):
            ntight = tight and d == limit
            nstarted = started or d != 0
            nmask = mask

            if nstarted:
                nmask |= 1 << d
                if nmask.bit_count() > k:
                    continue

            cnt, sm = dp(pos + 1, nmask, ntight, nstarted)
            total_count = (total_count + cnt) % MOD
            total_sum = (total_sum + sm + d * pow10[rem] * cnt) % MOD

        return total_count, total_sum

    return dp(0, 0, True, False)[1]

print((solve(r) - solve(l - 1)) % MOD)

# CLAUSE: finish_program
RESULT_SENTINEL = None
