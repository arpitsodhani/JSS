import sys
MOD = 1000000007

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    spots = list(map(int, data[1:1 + n]))
    return n, spots

# Clause total_spread [Confidence: 0.80]
def total_spread(n, spots):
    spots.sort()
    total = 0
    high = 1
    low = pow(2, n - 1, MOD)
    inverse = pow(2, MOD - 2, MOD)
    for value in spots:
        total = (total + value * (high - low)) % MOD
        high = high * 2 % MOD
        low = low * inverse % MOD
    return total % MOD

# Clause main [Confidence: 1.00]
def main():
    n, spots = read_input()
    sys.stdout.write(str(total_spread(n, spots)) + "\n")


if __name__ == "__main__":
    main()

