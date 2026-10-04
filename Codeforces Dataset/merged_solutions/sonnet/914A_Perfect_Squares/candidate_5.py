import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:1 + n]))
    return n, values


# --- clause: is_square :: (value: int) -> bool ---
def is_square(value):
    if value < 0:
        return False
    guess = int(round(value ** 0.5))
    for root in (guess - 1, guess, guess + 1):
        if root >= 0 and root * root == value:
            return True
    return False


# --- clause: largest_plain :: (n: int, values: list[int]) -> int ---
def largest_plain(n, values):
    best = None
    index = 0
    while index < n:
        value = values[index]
        if not is_square(value):
            if best is None or best < value:
                best = value
        index += 1
    return best


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    sys.stdout.write(str(largest_plain(n, values)) + "\n")


if __name__ == "__main__":
    main()
