import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(data[i + 1]) for i in range(n)]
    return n, values


# --- clause: sort_values :: (n: int, values: list[int]) -> list[int] ---
def sort_values(n, values):
    counts = [0] * 61
    for i in range(n):
        counts[values[i]] += 1
    ordered = []
    for value in range(1, 61):
        total = counts[value]
        for _ in range(total):
            ordered.append(value)
    return ordered


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    ordered = sort_values(n, values)
    sys.stdout.write("%s\n" % " ".join(map(str, ordered)))


if __name__ == "__main__":
    main()
