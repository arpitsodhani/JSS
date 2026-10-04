import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    sizes = []
    pos = 1
    for _ in range(t):
        sizes.append(int(data[pos]))
        pos += 1
    return sizes


# --- clause: build_triple :: (n: int) -> str ---
def build_triple(n):
    half, spare = divmod(n, 2)
    if spare:
        return "-1"
    return "0 %d %d" % (half, 0)


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(build_triple(n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
