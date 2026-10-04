import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[1].decode(), numbers[2].decode()


# --- clause: pair_cost :: (x: str, y: str, p: str, q: str) -> int ---
def pair_cost(x, y, p, q):
    if p == q:
        return 0 if x == y else 1
    if (x == p and y == q) or (x == q and y == p):
        return 0
    if x == p or x == q or y == p or y == q:
        return 1
    return 2


# --- clause: preprocess_moves :: (a: str, b: str) -> int ---
def preprocess_moves(a, b):
    n = len(a)
    summed = 0
    for i in range(n // 2):
        j = n - 1 - i
        summed += pair_cost(a[i], a[j], b[i], b[j])
    if n % 2 and a[n // 2] != b[n // 2]:
        summed += 1
    return summed


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % preprocess_moves(a, b))


if __name__ == "__main__":
    main()
