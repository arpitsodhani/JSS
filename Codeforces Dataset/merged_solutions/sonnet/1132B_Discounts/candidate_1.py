import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    prices = data[1:1 + n]
    m = data[1 + n]
    return prices, data[2 + n:2 + n + m]


# --- clause: coupon_costs :: (prices: list[int], coupons: list[int]) -> list[int] ---
def coupon_costs(prices, coupons):
    ranked = sorted(prices, reverse=True)
    total = sum(prices)
    return [total - ranked[q - 1] for q in coupons]


# --- clause: main :: () -> None ---
def main():
    prices, coupons = read_input()
    sys.stdout.write("\n".join(map(str, coupon_costs(prices, coupons))) + "\n")


if __name__ == "__main__":
    main()
