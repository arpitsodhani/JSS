import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    q = int(numbers[0])
    cursor = 1
    cases = []
    for _ in range(q):
        s = numbers[cursor + 1].decode()
        t = numbers[cursor + 2].decode()
        cursor += 3
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
    seen = False
    for i in range(len(t)):
        if s[i] == "1":
            seen = True
        if t[i] == "1" and not seen:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for s, t in read_input():
        out.append("YES" if is_interesting(s, t) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
