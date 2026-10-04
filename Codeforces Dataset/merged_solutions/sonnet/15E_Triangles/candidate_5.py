# CLAUSE: setup_environment
import sys

MOD = 1000000009

# CLAUSE: solve_logic
def main():
    n = int(sys.stdin.buffer.readline())
    rounds = n // 2 - 1
    powers = [2]

    for _ in range(rounds):
        powers.append((powers[-1] * 2) % MOD)

    current = 4
    total = 2

    for value in powers[1:]:
        current = (current * (value - 3)) % MOD
        total = (total + current) % MOD

    result = (2 * ((total * total) % MOD + 1)) % MOD
    sys.stdout.write(str(result) + "\n")

# CLAUSE: finish_program
main()
