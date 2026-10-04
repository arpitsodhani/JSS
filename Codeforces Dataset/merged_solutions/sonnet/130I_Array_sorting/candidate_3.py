import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = []
    for token in data[1:n + 1]:
        values.append(int(token))
    return n, values


# --- clause: sort_values :: (n: int, values: list[int]) -> list[int] ---
def sort_values(n, values):
    counts = [0] * 61
    for value in values:
        counts[value] += 1
    ordered = []
    value = 1
    while value <= 60:
        for _ in range(counts[value]):
            ordered.append(value)
        value += 1
    return ordered


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    ordered = sort_values(n, values)
    print(" ".join(map(str, ordered)))


if __name__ == "__main__":
    main()
