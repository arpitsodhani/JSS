# CLAUSE: setup_environment
import sys

BITS = 22
SIZE = 1 << BITS
FULL = SIZE - 1

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    values = data[1:1 + n]

    dp = [-1] * SIZE
    for value in values:
        dp[value] = value

    for bit in range(BITS):
        flag = 1 << bit
        for mask in range(SIZE):
            if mask & flag and dp[mask] == -1:
                dp[mask] = dp[mask ^ flag]

    sys.stdout.write(" ".join(str(dp[FULL ^ value]) for value in values))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
