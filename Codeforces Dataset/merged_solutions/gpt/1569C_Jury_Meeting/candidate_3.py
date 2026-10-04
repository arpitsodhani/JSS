# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    MOD = 998244353

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1

    max_n = 0
    cases = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        cases.append((n, a))
        if n > max_n:
            max_n = n

    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD

    out = []
    for n, a in cases:
        mx = max(a)
        cmx = a.count(mx)

        if cmx > 1:
            out.append(str(fact[n]))
            continue

        cnt_prev = a.count(mx - 1)
        if cnt_prev == 0:
            out.append("0")
            continue

        bad = fact[n] * pow(cnt_prev + 1, MOD - 2, MOD) % MOD
        out.append(str((fact[n] - bad) % MOD))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
