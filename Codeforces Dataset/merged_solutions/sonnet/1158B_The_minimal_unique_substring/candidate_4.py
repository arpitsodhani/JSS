import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1])

# --- clause: build_string :: (n: int, k: int) -> str ---
def build_string(n, k):
    if k == 1:
        return "1".ljust(n, "0")
    period = (n - k) // 2 + 1
    pieces = []
    for i in range(n):
        pieces.append("1" if i % period == 0 else "0")
    return "".join(pieces)

# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write(build_string(n, k) + "\n")


if __name__ == "__main__":
    main()
