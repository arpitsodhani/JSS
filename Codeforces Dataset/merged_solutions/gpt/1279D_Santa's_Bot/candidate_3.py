# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    MOD = 998244353

    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pos = 1

    cnt = {}
    prob = {}

    for _ in range(n):
        k = data[pos]
        pos += 1
        inv_k = pow(k, MOD - 2, MOD)
        for _ in range(k):
            x = data[pos]
            pos += 1
            cnt[x] = cnt.get(x, 0) + 1
            prob[x] = (prob.get(x, 0) + inv_k) % MOD

    ans = 0
    for x in prob:
        ans = (ans + prob[x] * cnt[x]) % MOD

    inv_n = pow(n, MOD - 2, MOD)
    ans = ans * inv_n % MOD * inv_n % MOD
    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
