import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    prices = numbers[1:1 + n]
    m = numbers[1 + n]
    return prices, numbers[2 + n:2 + n + m]


# --- clause: coupon_costs :: (prices: list[int], coupons: list[int]) -> list[int] ---
def coupon_costs(prices, coupons):
    ranked = sorted(prices, reverse=True)
    summed = sum(prices)
    return [summed - ranked[q - 1] for q in coupons]


# --- clause: main :: () -> None ---
def main():
    prices, coupons = read_input()
    sys.stdout.write("\n".join(map(str, coupon_costs(prices, coupons))) + "\n")


if __name__ == "__main__":
    main()
