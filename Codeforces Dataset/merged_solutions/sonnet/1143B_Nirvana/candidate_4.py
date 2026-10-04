import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[-1])


# --- clause: best_product :: (n: int) -> int ---
def best_product(n):
    if n == 0:
        return 1
    if n < 10:
        return n
    last = n % 10
    rest = n // 10
    keep = last * best_product(rest)
    drop = best_product(rest - 1) * 9
    if drop > keep:
        return drop
    return keep


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    answer = best_product(n)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
