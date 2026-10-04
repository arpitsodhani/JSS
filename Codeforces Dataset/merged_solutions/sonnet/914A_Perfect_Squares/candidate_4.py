import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(data[i + 1]) for i in range(n)]
    return n, values


# --- clause: is_square :: (value: int) -> bool ---
def is_square(value):
    if value < 0:
        return False
    root = 0
    while root * root < value:
        root += 1
    return root * root == value


# --- clause: largest_plain :: (n: int, values: list[int]) -> int ---
def largest_plain(n, values):
    best = None
    for value in values:
        if is_square(value):
            continue
        if best is None or value > best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    answer = largest_plain(n, values)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
