import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    return m, data[2:2 + n]


# --- clause: best_earnings :: (m: int, prices: list[int]) -> int ---
def best_earnings(m, prices):
    total = 0
    for value in sorted(prices)[:m]:
        if value < 0:
            total -= value
    return total


# --- clause: main :: () -> None ---
def main():
    m, prices = read_input()
    sys.stdout.write("%d\n" % best_earnings(m, prices))


if __name__ == "__main__":
    main()
