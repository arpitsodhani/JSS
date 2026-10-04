import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    pos = 1
    cases = []
    for _ in range(q):
        s = data[pos + 1].decode()
        t = data[pos + 2].decode()
        pos += 3
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
    out = []
    for s, t in read_input():
        out.append("YES" if is_interesting(s, t) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
