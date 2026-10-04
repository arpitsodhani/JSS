import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = []
    for token in data[1:n + 1]:
        values.append(int(token))
    return n, values


# --- clause: best_xor :: (n: int, values: list[int]) -> int ---
def best_xor(n, values):
    best = 0
    start = 0
    while start < n:
        running = 0
        end = start
        while end < n:
            running ^= values[end]
            if running > best:
                best = running
            end += 1
        start += 1
    return best


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    print(best_xor(n, values))


if __name__ == "__main__":
    main()
