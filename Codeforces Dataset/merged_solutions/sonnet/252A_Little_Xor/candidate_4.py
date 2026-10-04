import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = [int(data[i + 1]) for i in range(n)]
    return n, values


# --- clause: best_xor :: (n: int, values: list[int]) -> int ---
def best_xor(n, values):
    best = 0
    for start in range(n - 1, -1, -1):
        running = 0
        for end in range(start, n):
            running ^= values[end]
            if running > best:
                best = running
    return best


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    answer = best_xor(n, values)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
