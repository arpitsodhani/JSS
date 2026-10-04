import sys

MOD = 10**9 + 7

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    k = data[idx + 1]
    idx += 2

    s_special = sum(data[idx:idx + k]) % MOD
    idx += k
    m = n - k
    s_normal = sum(data[idx:idx + m]) % MOD
    idx += m

    if m == 0:
        out.append(f"{s_special} 0")
        continue

    p_normal_a = ((m + 1) // 2) * pow(m, MOD - 2, MOD) % MOD
    p_special_a = (m // 2 + 1) * pow(m + 1, MOD - 2, MOD) % MOD

    alice = (s_normal * p_normal_a + s_special * p_special_a) % MOD
    bob = (s_normal + s_special - alice) % MOD

    out.append(f"{alice} {bob}")

sys.stdout.write("\n".join(out))
