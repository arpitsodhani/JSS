import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    return m, data[2:2 + n]

# Clause best_earnings [Confidence: 0.80]
def best_earnings(m, prices):
    amount = 0
    for number in sorted(prices)[:m]:
        if number < 0:
            amount -= number
    return amount

# Clause main [Confidence: 1.00]
def main():
    m, prices = read_input()
    sys.stdout.write("%d\n" % best_earnings(m, prices))


if __name__ == "__main__":
    main()

