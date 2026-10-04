# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    MOD = 10**9 + 7
    B = 61

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1

    pow2 = [1] * B
    for i in range(1, B):
        pow2[i] = (pow2[i - 1] * 2) % MOD

    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        cnt = [0] * B
        for x in a:
            for b in range(B):
                if (x >> b) & 1:
                    cnt[b] += 1

        ans = 0
        for x in a:
            s_and = 0
            s_or = 0
            for b in range(B):
                if (x >> b) & 1:
                    s_and = (s_and + pow2[b] * cnt[b]) % MOD
                    s_or = (s_or + pow2[b] * n) % MOD
                else:
                    s_or = (s_or + pow2[b] * cnt[b]) % MOD
            ans = (ans + s_and * s_or) % MOD

        out.append(str(ans))

    print("\n".join(out))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
