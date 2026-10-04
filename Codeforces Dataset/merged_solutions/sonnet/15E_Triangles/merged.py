# Clause setup_environment [Confidence: 0.80]
import sys

MOD = 1000000009


# Clause solve_logic [Confidence: 0.60]
def main():
    n = int(sys.stdin.readline())
    power = 2
    ways = 2
    add = 4

    for _ in range(n // 2 - 1):
        power = (power * 2) % MOD
        add = add * (power - 3) % MOD
        ways = (ways + add) % MOD

    print((2 * (ways * ways + 1)) % MOD)


# Clause finish_program [Confidence: 0.40]
main()


