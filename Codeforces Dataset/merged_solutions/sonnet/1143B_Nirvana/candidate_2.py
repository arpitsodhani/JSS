import sys


# --- clause: read_input :: () -> int ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return n


# --- clause: best_product :: (n: int) -> int ---
def best_product(n):
    if n == 0:
        return 1
    if n < 10:
        return n
    head, tail = divmod(n, 10)
    keep = tail * best_product(head)
    drop = 9 * best_product(head - 1)
    return keep if keep > drop else drop


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("%d\n" % best_product(n))


if __name__ == "__main__":
    main()
