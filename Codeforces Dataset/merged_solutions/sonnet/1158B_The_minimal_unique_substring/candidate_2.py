import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[0]), int(data[1])

# --- clause: build_string :: (n: int, k: int) -> str ---
def build_string(n, k):
    if k == 1:
        return "1" + "0" * (n - 1)
    period = (n - k) // 2 + 1
    letters = ["0"] * n
    for i in range(0, n, period):
        letters[i] = "1"
    return "".join(letters)

# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write(build_string(n, k) + "\n")


if __name__ == "__main__":
    main()
