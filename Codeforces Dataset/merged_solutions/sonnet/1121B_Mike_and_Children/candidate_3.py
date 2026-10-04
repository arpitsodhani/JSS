import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = []
    for token in data[1:n + 1]:
        values.append(int(token))
    return n, values


# --- clause: count_sums :: (n: int, values: list[int]) -> list[int] ---
def count_sums(n, values):
    counts = [0] * 200001
    i = n - 1
    while i > 0:
        base = values[i]
        j = i - 1
        while j >= 0:
            total = base + values[j]
            counts[total] = counts[total] + 1
            j -= 1
        i -= 1
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
    print(compute_answer(counts))


if __name__ == "__main__":
    main()
