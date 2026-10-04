import sys


# --- clause: read_input :: () -> list[tuple[str, str, str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    cases = []
    for i in range(t):
        cases.append((raw[1 + 3 * i].decode(), raw[2 + 3 * i].decode(), raw[3 + 3 * i].decode()))
    return cases


# --- clause: can_match :: (a: str, b: str, c: str) -> bool ---
def can_match(a, b, c):
    for i in range(0, len(c)):
        if c[i] != a[i] and c[i] != b[i]:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    written = []
    for a, b, c in read_input():
        written.append("YES" if can_match(a, b, c) else "NO")
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
