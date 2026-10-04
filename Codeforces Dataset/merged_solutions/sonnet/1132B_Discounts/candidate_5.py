import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    prices = raw[1:1 + n]
    m = raw[1 + n]
    return prices, raw[2 + n:2 + n + m]


# --- clause: coupon_costs :: (prices: list[int], coupons: list[int]) -> list[int] ---
def coupon_costs(prices, coupons):
    ranked = sorted(prices, reverse=True)
    running = sum(prices)
    return [running - ranked[q - 1] for q in coupons]


# --- clause: main :: () -> None ---
def main():
    prices, coupons = read_input()
    sys.stdout.write("\n".join(map(str, coupon_costs(prices, coupons))) + "\n")


if __name__ == "__main__":
    main()
