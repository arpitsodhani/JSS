import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause best_kills [Confidence: 1.00]
def best_kills(n):
    mod = 1000000007
    six = pow(6, mod - 2, mod)
    squares = n % mod * ((n + 1) % mod) % mod * ((2 * n + 1) % mod) % mod * six % mod
    steps = (n - 1) % mod * (n % mod) % mod * ((n + 1) % mod) % mod * pow(3, mod - 2, mod) % mod
    return (squares + steps) % mod * 2022 % mod

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for n in read_input():
        collected.append(best_kills(n))
    sys.stdout.write("\n".join(map(str, collected)) + "\n")


if __name__ == "__main__":
    main()

