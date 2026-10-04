import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(token) for token in data[1:n + 1]]
    return n, values


# --- clause: sort_values :: (n: int, values: list[int]) -> list[int] ---
def sort_values(n, values):
    counts = [0] * 61
    for value in values:
        counts[value] += 1
    ordered = []
    for value in range(1, 61):
        for _ in range(counts[value]):
            ordered.append(value)
    return ordered


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    ordered = sort_values(n, values)
    sys.stdout.write(" ".join(map(str, ordered)) + "\n")


if __name__ == "__main__":
    main()
