# CLAUSE: setup_environment
import sys

MOD = 1000000009

# CLAUSE: solve_logic
def count_routes(levels):
    half = levels // 2
    term = 4
    total = 2
    power = 2
    step = 1

    while step < half:
        power = (power << 1) % MOD
        term = (term * (power - 3)) % MOD
        total = (total + term) % MOD
        step += 1

    return (2 * (total * total + 1)) % MOD

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    sys.stdout.write(str(count_routes(n)))

# CLAUSE: finish_program
main()
