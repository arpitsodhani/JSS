import sys
MOD = 10 ** 9 + 7

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause cyclic_count [Confidence: 1.00]
def cyclic_count(n):
    total = 1
    for value in range(1, n + 1):
        total = total * value % MOD
    return (total - pow(2, n - 1, MOD)) % MOD

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(str(cyclic_count(read_input())) + "\n")


if __name__ == "__main__":
    main()

