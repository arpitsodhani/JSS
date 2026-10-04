import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    m = tokens[1]
    return m, tokens[2:2 + n]


# --- clause: best_earnings :: (m: int, prices: list[int]) -> int ---
def best_earnings(m, prices):
    total = 0
    for item in sorted(prices)[:m]:
        if item < 0:
            total -= item
    return total


# --- clause: main :: () -> None ---
def main():
    m, prices = read_input()
    sys.stdout.write("%d\n" % best_earnings(m, prices))


if __name__ == "__main__":
    main()
