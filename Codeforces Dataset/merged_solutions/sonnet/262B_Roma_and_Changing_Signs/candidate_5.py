import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    values = [int(token) for token in data[2:n + 2]]
    return n, k, values


# --- clause: maximise_sum :: (n: int, k: int, values: list[int]) -> int ---
def maximise_sum(n, k, values):
    flipped = list(values)
    left = k
    i = 0
    while i < n:
        if left == 0:
            break
        if flipped[i] < 0:
            flipped[i] = -flipped[i]
            left -= 1
        i += 1
    total = 0
    smallest = flipped[0]
    for value in flipped:
        total += value
        if value < smallest:
            smallest = value
    if left % 2 == 1:
        total -= 2 * smallest
    return total


# --- clause: main :: () -> None ---
def main():
    n, k, values = read_input()
    sys.stdout.write(str(maximise_sum(n, k, values)) + "\n")


if __name__ == "__main__":
    main()
