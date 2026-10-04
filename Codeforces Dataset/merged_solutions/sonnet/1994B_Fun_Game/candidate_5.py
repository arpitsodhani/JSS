import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    q = int(raw[0])
    reader = 1
    cases = []
    for _ in range(q):
        s = raw[reader + 1].decode()
        t = raw[reader + 2].decode()
        reader += 3
        cases.append((s, t))
    return cases


# --- clause: first_one :: (bits: str) -> int ---
def first_one(bits):
    for i in range(0, len(bits)):
        if bits[i] == "1":
            return i
    return len(bits)


# --- clause: is_interesting :: (s: str, t: str) -> bool ---
def is_interesting(s, t):
    return first_one(s) <= first_one(t)


# --- clause: main :: () -> None ---
def main():
    lines = []
    for s, t in read_input():
        lines.append("YES" if is_interesting(s, t) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
