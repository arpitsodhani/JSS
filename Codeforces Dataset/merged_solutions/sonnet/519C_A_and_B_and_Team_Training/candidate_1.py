import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1])


# --- clause: compute_answer :: (n: int, m: int) -> int ---
def compute_answer(n, m):
    pairs = (n + m) // 3
    return min(n, m, pairs)


# --- clause: main :: () -> None ---
def main():
    n, m = read_input()
    print(compute_answer(n, m))


if __name__ == "__main__":
    main()
