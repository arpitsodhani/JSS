import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0])


# --- clause: best_product :: (n: int) -> int ---
def best_product(n):
    if n == 0:
        return 1
    if n < 10:
        return n
    keep = (n % 10) * best_product(n // 10)
    drop = 9 * best_product(n // 10 - 1)
    if keep > drop:
        return keep
    return drop


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write(str(best_product(n)) + "\n")


if __name__ == "__main__":
    main()
