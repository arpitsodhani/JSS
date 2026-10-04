import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    sizes = []
    for token in data[1:1 + t]:
        sizes.append(int(token))
    return sizes


# --- clause: build_sequence :: (n: int) -> list[int] ---
def build_sequence(n):
    values = []
    values.append(3 * n)
    values.append(5 * n)
    middle = n - 2
    if middle % 2 == 0:
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
    for n in read_input():
        out.append(" ".join(map(str, build_sequence(n))))
    print("\n".join(out))


if __name__ == "__main__":
    main()
