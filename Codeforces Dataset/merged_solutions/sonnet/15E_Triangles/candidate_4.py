# CLAUSE: setup_environment
import sys

MOD = 1000000009

# CLAUSE: solve_logic
def sequence_value(limit):
    state = [2, 2, 4]
    for index in range(1, limit):
        state[0] = (state[0] * 2) % MOD
        state[2] = (state[2] * (state[0] - 3)) % MOD
        state[1] += state[2]
        state[1] %= MOD
    return state[1]

def main():
    n = int(sys.stdin.readline())
    ways = sequence_value(n // 2)
    answer = (2 * (pow(ways, 2, MOD) + 1)) % MOD
    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
