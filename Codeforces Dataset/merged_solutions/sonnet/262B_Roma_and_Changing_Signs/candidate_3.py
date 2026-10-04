import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    values = []
    for token in data[2:n + 2]:
        values.append(int(token))
    return n, k, values


# --- clause: maximise_sum :: (n: int, k: int, values: list[int]) -> int ---
def maximise_sum(n, k, values):
    flipped = list(values)
    left = k
    for i in range(n):
        if left == 0:
            break
        if flipped[i] < 0:
            flipped[i] = -flipped[i]
            left -= 1
    total = sum(flipped)
    smallest = flipped[0]
    for value in flipped:
        if smallest > value:
            smallest = value
    if left & 1:
        total = total - 2 * smallest
    return total


# --- clause: main :: () -> None ---
def main():
    n, k, values = read_input()
    print(maximise_sum(n, k, values))


if __name__ == "__main__":
    main()
