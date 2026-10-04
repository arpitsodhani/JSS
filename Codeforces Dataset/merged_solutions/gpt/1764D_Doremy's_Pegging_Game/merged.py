# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    n, p = map(int, sys.stdin.readline().split())

    fac = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % p

    invfac = [1] * (n + 1)
    invfac[n] = pow(fac[n], p - 2, p)
    for i in range(n, 0, -1):
        invfac[i - 1] = invfac[i] * i % p

    t = n // 2
    ans = 0

    for i in range(t, n):
        if n % 2 == 1 and i == n - 1:
            break

        if i == n - 1:
            upper = n - i - 1
        else:
            upper = n - i - 2

        cur = 0
        fu = fac[upper]
        base = i - 1

        for j in range(upper + 1):
            cur = (cur + fu * invfac[j] % p * invfac[upper - j] % p * fac[base + j]) % p

        ans = (ans + n * (2 * t - i) * cur) % p

    print(ans % p)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
