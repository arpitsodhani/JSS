import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    values = [int(data[i + 2]) for i in range(n)]
    return n, k, values


# --- clause: maximise_sum :: (n: int, k: int, values: list[int]) -> int ---
def maximise_sum(n, k, values):
    flipped = values[:]
    left = k
    for i in range(n):
        if left == 0:
            break
        if flipped[i] < 0:
            flipped[i] = -flipped[i]
            left -= 1
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
    answer = maximise_sum(n, k, values)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
