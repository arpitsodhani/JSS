import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    count = int(data[0])
    values = list(map(int, data[1:count + 1]))
    return count, values


# --- clause: sort_values :: (n: int, values: list[int]) -> list[int] ---
def sort_values(n, values):
    counts = [0] * 61
    for value in values:
        counts[value] = counts[value] + 1
    ordered = []
    for value in range(1, 61):
        for _ in range(counts[value]):
            ordered.append(value)
    return ordered


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    result = sort_values(n, values)
    sys.stdout.write(" ".join([str(value) for value in result]) + "\n")


if __name__ == "__main__":
    main()
