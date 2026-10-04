# CLAUSE: setup_environment
import sys

MOD = 1000000009

# CLAUSE: solve_logic
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

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
