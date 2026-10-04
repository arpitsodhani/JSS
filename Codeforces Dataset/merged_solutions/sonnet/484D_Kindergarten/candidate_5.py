import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: best_total :: (n: int, a: list[int]) -> int ---
def best_total(n, a):
    best_minus = -a[0]
    best_plus = a[0]
    total = 0
    for i in range(1, n + 1):
        value = a[i - 1]
        first = best_minus + value
        second = best_plus - value
        total = first if first > second else second
        if i < n:
            nxt = a[i]
            low = total - nxt
            high = total + nxt
            if low > best_minus:
                best_minus = low
            if high > best_plus:
                best_plus = high
    return total


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    sys.stdout.write(str(best_total(n, a)) + "\n")


if __name__ == "__main__":
    main()
