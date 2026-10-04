import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: build_array :: (n: int) -> list[int] ---
def build_array(n):
    lines = []
    for value in range(n, 0, -1):
        lines.append(value)
    lines.append(n)
    for value in range(1, n):
        lines.append(value)
    return lines


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n in read_input():
        lines.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
