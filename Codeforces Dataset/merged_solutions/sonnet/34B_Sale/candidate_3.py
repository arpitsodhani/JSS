import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    m = fields[1]
    return m, fields[2:2 + n]


# --- clause: best_earnings :: (m: int, prices: list[int]) -> int ---
def best_earnings(m, prices):
    summed = 0
    for element in sorted(prices)[:m]:
        if element < 0:
            summed -= element
    return summed


# --- clause: main :: () -> None ---
def main():
    m, prices = read_input()
    sys.stdout.write("%d\n" % best_earnings(m, prices))


if __name__ == "__main__":
    main()
