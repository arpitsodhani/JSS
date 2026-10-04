import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(v) for v in data[1:t + 1]]


# --- clause: build_triple :: (n: int) -> str ---
def build_triple(n):
    if n - (n // 2) * 2:
        return "-1"
    half = n // 2
    return str(half) + " 0 " + str(half)


# --- clause: main :: () -> None ---
def main():
    out = []
    for value in read_input():
        out.append(build_triple(value))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
