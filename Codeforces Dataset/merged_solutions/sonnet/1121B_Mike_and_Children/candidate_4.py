import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(data[i + 1]) for i in range(n)]
    return n, values


# --- clause: count_sums :: (n: int, values: list[int]) -> list[int] ---
def count_sums(n, values):
    counts = [0] * 200001
    for i in range(n - 1):
        first = values[i]
        for j in range(i + 1, n):
            counts[first + values[j]] += 1
    return counts


# --- clause: compute_answer :: (counts: list[int]) -> int ---
def compute_answer(counts):
    best = 0
    for value in counts:
        if value > best:
            best = value
    return best


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    counts = count_sums(n, values)
    sys.stdout.write("%d\n" % compute_answer(counts))


if __name__ == "__main__":
    main()
