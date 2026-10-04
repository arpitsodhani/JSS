import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1:1 + n]))
    return n, values


# --- clause: best_xor :: (n: int, values: list[int]) -> int ---
def best_xor(n, values):
    best = 0
    for start in range(n):
        running = 0
        for end in range(start, n):
            running = running ^ values[end]
            if running > best:
                best = running
    return best


# --- clause: main :: () -> None ---
def main():
    n, values = read_input()
    best = best_xor(n, values)
    sys.stdout.write(str(best) + "\n")


if __name__ == "__main__":
    main()
