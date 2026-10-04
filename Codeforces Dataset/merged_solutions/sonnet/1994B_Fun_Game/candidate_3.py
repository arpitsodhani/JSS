import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    q = int(fields[0])
    offset = 1
    cases = []
    for _ in range(q):
        s = fields[offset + 1].decode()
        t = fields[offset + 2].decode()
        offset += 3
        cases.append((s, t))
    return cases


# --- clause: first_one :: (bits: str) -> int ---
def first_one(bits):
    for i in range(len(bits)):
        if bits[i] == "1":
            return i
    return len(bits)


# --- clause: is_interesting :: (s: str, t: str) -> bool ---
def is_interesting(s, t):
    return first_one(s) <= first_one(t)


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for s, t in read_input():
        pieces.append("YES" if is_interesting(s, t) else "NO")
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
