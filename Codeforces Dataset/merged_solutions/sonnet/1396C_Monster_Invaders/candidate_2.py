# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n, r1, r2, r3, d = values[:5]
    monsters = values[5:]

    full = [min(x * r1 + r3, (x + 2) * r1) for x in monsters]
    partial = [min((x + 1) * r1, r2) for x in monsters]

    inf = 10 ** 30
    dp0, dp1 = 0, inf

    for i in range(n - 1):
        dp0, dp1 = (
            min(dp0 + full[i] + d, dp1 + full[i] + 2 * d),
            min(dp0 + partial[i] + 2 * d, dp1 + partial[i] + 2 * d),
        )

    last = n - 1
    ans = min(
        dp0 + full[last],
        dp1 + full[last] + d,
        dp0 + partial[last] + r1,
        dp1 + partial[last] + r1 + d,
    )
    sys.stdout.write(str(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
