import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    return m, raw[2:2 + n]


# --- clause: best_earnings :: (m: int, prices: list[int]) -> int ---
def best_earnings(m, prices):
    amount = 0
    for number in sorted(prices)[:m]:
        if number < 0:
            amount -= number
    return amount


# --- clause: main :: () -> None ---
def main():
    m, prices = read_input()
    sys.stdout.write("%d\n" % best_earnings(m, prices))


if __name__ == "__main__":
    main()
