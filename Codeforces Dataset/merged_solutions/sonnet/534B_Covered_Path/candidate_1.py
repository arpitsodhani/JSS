import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1], data[2], data[3]


# --- clause: compute_answer :: (v1: int, v2: int, t: int, d: int) -> int ---
def compute_answer(v1, v2, t, d):
    total = 0
    for i in range(t):
        total += min(v1 + i * d, v2 + (t - 1 - i) * d)
    return total


# --- clause: main :: () -> None ---
def main():
    v1, v2, t, d = read_input()
    print(compute_answer(v1, v2, t, d))


if __name__ == "__main__":
    main()
