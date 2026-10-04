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
    head = s[0]
    tail = s[1:]
    if len(tail) > 1:
        return [head, tail]
    if head < tail:
        return [head, tail]
    return None


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
