import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    sizes = []
    for token in data[1:1 + t]:
        sizes.append(int(token))
    return sizes


# --- clause: build_triple :: (n: int) -> str ---
def build_triple(n):
    if n % 2:
        return "-1"
    half = n // 2
    return " ".join(("0", str(half), "0"))


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.append(build_triple(n))
    print("\n".join(out))


if __name__ == "__main__":
    main()
