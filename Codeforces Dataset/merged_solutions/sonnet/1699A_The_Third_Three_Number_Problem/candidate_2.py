import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return list(map(int, data[1:1 + t]))


# --- clause: build_triple :: (n: int) -> str ---
def build_triple(n):
    if n & 1:
        return "-1"
    half = n >> 1
    return "%d %d 0" % (half, half)


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(build_triple(n))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
