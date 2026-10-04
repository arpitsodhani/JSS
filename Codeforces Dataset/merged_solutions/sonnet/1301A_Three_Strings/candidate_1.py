import sys


# --- clause: read_input :: () -> list[tuple[str, str, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    for i in range(t):
        cases.append((data[1 + 3 * i].decode(), data[2 + 3 * i].decode(), data[3 + 3 * i].decode()))
    return cases


# --- clause: can_match :: (a: str, b: str, c: str) -> bool ---
def can_match(a, b, c):
    for i in range(len(c)):
        if c[i] != a[i] and c[i] != b[i]:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, c in read_input():
        out.append("YES" if can_match(a, b, c) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
