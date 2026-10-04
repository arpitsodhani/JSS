import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    return [raw[1 + i].decode() for i in range(t)]


# --- clause: build_string :: (t: str) -> str ---
def build_string(t):
    if t.count("0") == 0 or t.count("1") == 0:
        return t
    return "01" * len(t)


# --- clause: main :: () -> None ---
def main():
    written = []
    for t in read_input():
        written.append(build_string(t))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
