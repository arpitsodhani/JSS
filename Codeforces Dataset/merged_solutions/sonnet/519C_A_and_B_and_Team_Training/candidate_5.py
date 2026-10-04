import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    x = int(raw[0])
    y = int(raw[1])
    return x, y


# --- clause: compute_answer :: (n: int, m: int) -> int ---
def compute_answer(n, m):
    total = (n + m) // 3
    return min([n, m, total])


# --- clause: main :: () -> None ---
def main():
    x, y = read_input()
    out = compute_answer(x, y)
    sys.stdout.write("%d\n" % out)


if __name__ == "__main__":
    main()
