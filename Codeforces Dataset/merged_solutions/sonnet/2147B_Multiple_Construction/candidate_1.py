import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]


# --- clause: build_array :: (n: int) -> list[int] ---
def build_array(n):
    out = []
    for value in range(n, 0, -1):
        out.append(value)
    out.append(n)
    for value in range(1, n):
        out.append(value)
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
