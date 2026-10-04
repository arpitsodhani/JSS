import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    return [numbers[1 + i].decode() for i in range(t)]


# --- clause: build_string :: (t: str) -> str ---
def build_string(t):
    kinds = set(t)
    if len(kinds) < 2:
        return t
    out = []
    while len(out) < 2 * len(t):
        out.append("0")
        out.append("1")
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for t in read_input():
        pieces.append(build_string(t))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
