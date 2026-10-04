import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    return m, numbers[2:2 + n]


# --- clause: best_earnings :: (m: int, prices: list[int]) -> int ---
def best_earnings(m, prices):
    negatives = []
    for value in prices:
        if value < 0:
            negatives.append(-value)
    negatives.sort(reverse=True)
    total = 0
    for value in negatives[:m]:
        total += value
    return total


# --- clause: main :: () -> None ---
def main():
    m, prices = read_input()
    sys.stdout.write("%d\n" % best_earnings(m, prices))


if __name__ == "__main__":
    main()
