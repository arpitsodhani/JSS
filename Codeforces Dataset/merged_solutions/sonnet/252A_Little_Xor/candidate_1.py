import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(token) for token in data[1:n + 1]]
    return n, values


# --- clause: best_xor :: (n: int, values: list[int]) -> int ---
def best_xor(n, values):
    best = 0
    for start in range(n):
        running = 0
        for end in range(start, n):
            running ^= values[end]
            if running > best:
                best = running
    return best


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    sys.stdout.write(str(best_xor(n, values)) + "\n")


if __name__ == "__main__":
    main()
