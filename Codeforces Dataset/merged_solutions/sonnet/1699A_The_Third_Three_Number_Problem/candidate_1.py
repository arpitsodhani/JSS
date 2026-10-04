import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [int(data[i + 1]) for i in range(t)]


# --- clause: build_triple :: (n: int) -> str ---
def build_triple(n):
    if n % 2 == 1:
        return "-1"
    half = n // 2
    return "0 0 %d" % half


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(build_triple(n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
