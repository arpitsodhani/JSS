import sys


# --- clause: read_input :: () -> tuple[int, int, int, int] ---
def read_input():
    parts = list(map(int, sys.stdin.buffer.read().split()))
    first = parts[0]
    last = parts[1]
    length = parts[2]
    bound = parts[3]
    return first, last, length, bound


# --- clause: compute_answer :: (v1: int, v2: int, t: int, d: int) -> int ---
def compute_answer(v1, v2, t, d):
    acc = 0
    for pos in range(t):
        rise = v1 + d * pos
        fall = v2 + d * (t - pos - 1)
        acc += rise if rise <= fall else fall
    return acc


# --- clause: main :: () -> None ---
def main():
    first, last, length, bound = read_input()
    result = compute_answer(first, last, length, bound)
    sys.stdout.write("%d\n" % result)


if __name__ == "__main__":
    main()
