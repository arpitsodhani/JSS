import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]


# --- clause: build_string :: (t: str) -> str ---
def build_string(t):
    if t.count("0") == 0 or t.count("1") == 0:
        return t
    return "01" * len(t)


# --- clause: main :: () -> None ---
def main():
    out = []
    for t in read_input():
        out.append(build_string(t))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
