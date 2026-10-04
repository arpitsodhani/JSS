import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    return [tokens[1 + i].decode() for i in range(t)]


# --- clause: build_string :: (t: str) -> str ---
def build_string(t):
    if t.count("0") == 0 or t.count("1") == 0:
        return t
    return "01" * len(t)


# --- clause: main :: () -> None ---
def main():
    lines = []
    for t in read_input():
        lines.append(build_string(t))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
