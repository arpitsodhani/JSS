# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
MOD = 998244353

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

def parse_cases(data):
    t = data[0]
    idx = 1
    cases = []
    ok = True
    for _ in range(t):
        if idx >= len(data):
            ok = False
            break
        n = data[idx]
        idx += 1
        if idx + n > len(data):
            ok = False
            break
        cases.append(data[idx:idx + n])
        idx += n
    if ok and idx == len(data):
        return cases
    n = data[0]
    return [data[1:1 + n]]

cases = parse_cases(data)
out = []

for a in cases:
    z = a.count(0)
    pow2 = [1] * (z + 1)
    for i in range(1, z + 1):
        pow2[i] = (pow2[i - 1] * 2) % MOD

    ans = pow2[z]
    prior = {}
    zeros = 0

    for x in a:
        if x == 0:
            zeros += 1
        else:
            ans = (ans + pow2[z - zeros] * prior.get(x, 0)) % MOD
            prior[x] = (prior.get(x, 0) + pow2[zeros]) % MOD

    out.append(str(ans % MOD))

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
