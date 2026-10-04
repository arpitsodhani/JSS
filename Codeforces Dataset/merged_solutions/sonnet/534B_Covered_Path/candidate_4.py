import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    return values[0], values[1], values[2], values[3]


# --- clause: compute_answer :: (v1: int, v2: int, t: int, d: int) -> int ---
def compute_answer(v1, v2, t, d):
    path = 0
    for j in range(t - 1, -1, -1):
        from_start = v1 + d * (t - 1 - j)
        from_end = v2 + d * j
        path += min(from_start, from_end)
    return path


# --- clause: main :: () -> None ---
def main():
    params = read_input()
    print(compute_answer(params[0], params[1], params[2], params[3]))


if __name__ == "__main__":
    main()
