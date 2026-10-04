import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    parts = sys.stdin.buffer.read().split()
    x = parts[0].decode()
    y = parts[1].decode()
    return x, y


# --- clause: compute_answer :: (x: str, y: str) -> str ---
def compute_answer(x, y):
    result = []
    for xc, yc in zip(x, y):
        if yc > xc:
            return "-1"
        result.append(yc)
    return "".join(result)


# --- clause: main :: () -> None ---
def main():
    pair = read_input()
    print(compute_answer(pair[0], pair[1]))


if __name__ == "__main__":
    main()
