import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    cases = []
    pos = 1
    for _ in range(q):
        pos += 1
        cases.append(data[pos].decode())
        pos += 1
    return cases


# --- clause: split_digits :: (s: str) -> list[str] | None ---
def split_digits(s):
    n = len(s)
    if n > 2:
        return [s[:1], s[1:]]
    return [s[:1], s[1:]] if int(s[0]) < int(s[1]) else None


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        parts = split_digits(s)
        if parts is None:
            out.append("NO")
        else:
            out.append("YES")
            out.append(str(len(parts)))
            out.append(" ".join(parts))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
