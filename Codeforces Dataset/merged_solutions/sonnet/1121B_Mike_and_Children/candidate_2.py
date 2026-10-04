import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    count = int(data[0])
    values = list(map(int, data[1:count + 1]))
    return count, values


# --- clause: count_sums :: (n: int, values: list[int]) -> list[int] ---
def count_sums(n, values):
    counts = [0] * 200001
    for i in range(n):
        left = values[i]
        for j in range(i + 1, n):
            total = left + values[j]
            counts[total] += 1
    return counts


# --- clause: compute_answer :: (counts: list[int]) -> int ---
def compute_answer(counts):
    best = 0
    for value in counts:
        if best < value:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    tally = count_sums(n, values)
    sys.stdout.write(str(compute_answer(tally)) + "\n")


if __name__ == "__main__":
    main()
