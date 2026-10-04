import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: build_array :: (n: int) -> list[int] ---
def build_array(n):
    written = []
    for item in range(n, 0, -1):
        written.append(item)
    written.append(n)
    for item in range(1, n):
        written.append(item)
    return written


# --- clause: main :: () -> None ---
def main():
    written = []
    for n in read_input():
        written.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
