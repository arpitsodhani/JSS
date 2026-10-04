import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(data[1 + i]) for i in range(t)]


# --- clause: build_sequence :: (n: int) -> list[int] ---
def build_sequence(n):
    values = [3 * n, 5 * n]
    middle = n - 2
    if middle % 2 == 0:
        half = middle >> 1
        for step in range(1, half + 1):
            values.append(4 * n - step)
            values.append(4 * n + step)
    else:
        values.append(n * 4)
        half = (middle - 1) >> 1
        for step in range(1, half + 1):
            values.append(4 * n - step)
            values.append(4 * n + step)
    return values


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(" ".join(map(str, build_sequence(n))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
