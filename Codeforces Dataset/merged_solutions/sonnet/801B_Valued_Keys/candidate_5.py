import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    x = raw[0].decode()
    y = raw[1].decode()
    return x, y


# --- clause: compute_answer :: (x: str, y: str) -> str ---
def compute_answer(x, y):
    z = []
    for a, b in zip(x, y):
        if min(a, b) != b:
            return "-1"
        z.append(b)
    return "".join(z)


# --- clause: main :: () -> None ---
def main():
    x, y = read_input()
    answer = compute_answer(x, y)
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
