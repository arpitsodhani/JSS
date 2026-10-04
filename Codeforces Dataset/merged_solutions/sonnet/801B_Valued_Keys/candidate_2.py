import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    source = tokens[0].decode()
    target = tokens[1].decode()
    return source, target


# --- clause: compute_answer :: (x: str, y: str) -> str ---
def compute_answer(x, y):
    z = []
    for i in range(len(x)):
        if y[i] > x[i]:
            return "-1"
        z.append(y[i])
    return "".join(z)


# --- clause: main :: () -> None ---
def main():
    source, target = read_input()
    sys.stdout.write(compute_answer(source, target) + "\n")


if __name__ == "__main__":
    main()
