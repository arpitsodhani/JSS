import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(v) for v in data[1:t + 1]]


# --- clause: build_sequence :: (n: int) -> list[int] ---
def build_sequence(n):
    values = [3 * n, 5 * n]
    middle = n - 2
    if not middle & 1:
        half = middle // 2
        for step in range(1, half + 1):
            values.append(4 * n - step)
            values.append(4 * n + step)
    else:
        values.append(4 * n)
        half = (middle - 1) // 2
        for step in range(1, half + 1):
            values.append(4 * n - step)
            values.append(4 * n + step)
    return values


# --- clause: main :: () -> None ---
def main():
    out = []
    for size in read_input():
        out.append(" ".join(map(str, build_sequence(size))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
