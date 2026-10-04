import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = []
    for token in data[1:n + 1]:
        values.append(int(token))
    return n, values


# --- clause: is_square :: (value: int) -> bool ---
def is_square(value):
    if value < 0:
        return False
    root = int(value ** 0.5)
    while root * root > value:
        root -= 1
    while (root + 1) * (root + 1) <= value:
        root += 1
    return root * root == value


# --- clause: largest_plain :: (n: int, values: list[int]) -> int ---
def largest_plain(n, values):
    ordered = sorted(values, reverse=True)
    for value in ordered:
        if not is_square(value):
            return value
    return ordered[0]


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    print(largest_plain(n, values))


if __name__ == "__main__":
    main()
