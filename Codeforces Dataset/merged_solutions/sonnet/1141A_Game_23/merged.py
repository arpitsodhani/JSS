# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.40]
def main():
    n, m = map(int, sys.stdin.read().split())
    if m % n:
        sys.stdout.write("-1")
        return
    q = m // n
    ans = 0
    for p in (2, 3):
        while q % p == 0:
            q //= p
            ans += 1
    sys.stdout.write(str(ans if q == 1 else -1))


# Clause finish_program [Confidence: 0.60]
main()


