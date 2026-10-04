# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    MOD = 998244353

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    if len(data) > 1 and data[0] == len(data) - 1:
        queries = data[1:]
    else:
        queries = data

    maxn = max(queries)
    f = [0] * (maxn + 1)
    init = [1, 1, 2, 4, 12, 32]

    for i in range(min(maxn + 1, 6)):
        f[i] = init[i]

    for n in range(maxn - 5):
        f[n + 6] = (
            f[n + 5]
            + (n + 1) * f[n + 4]
            + 6 * f[n + 3]
            + (4 * n + 12) * f[n + 2]
            + (4 * n + 8) * f[n]
        ) % MOD

    sys.stdout.write("\n".join(str(f[n]) for n in queries))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
