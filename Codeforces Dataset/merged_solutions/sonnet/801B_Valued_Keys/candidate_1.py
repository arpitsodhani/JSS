import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode(), data[1].decode()


# --- clause: compute_answer :: (x: str, y: str) -> str ---
def compute_answer(x, y):
    for a, b in zip(x, y):
        if b > a:
            return "-1"
    return y


# --- clause: main :: () -> None ---
def main():
    x, y = read_input()
    print(compute_answer(x, y))


if __name__ == "__main__":
    main()
