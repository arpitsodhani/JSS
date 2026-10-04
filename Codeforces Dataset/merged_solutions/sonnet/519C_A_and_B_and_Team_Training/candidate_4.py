import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    return values[0], values[1]


# --- clause: compute_answer :: (n: int, m: int) -> int ---
def compute_answer(n, m):
    capacity = (n + m) // 3
    return min(n, min(m, capacity))


# --- clause: main :: () -> None ---
def main():
    pair = read_input()
    print(compute_answer(pair[0], pair[1]))


if __name__ == "__main__":
    main()
