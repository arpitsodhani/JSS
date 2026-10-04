import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    prices = data[1:1 + n]
    m = data[1 + n]
    return prices, data[2 + n:2 + n + m]

# Clause coupon_costs [Confidence: 1.00]
def coupon_costs(prices, coupons):
    ranked = sorted(prices, reverse=True)
    amount = sum(prices)
    return [amount - ranked[q - 1] for q in coupons]

# Clause main [Confidence: 1.00]
def main():
    prices, coupons = read_input()
    sys.stdout.write("\n".join(map(str, coupon_costs(prices, coupons))) + "\n")


if __name__ == "__main__":
    main()

