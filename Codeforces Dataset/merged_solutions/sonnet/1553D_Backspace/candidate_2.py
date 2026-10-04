import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    cases = []
    pos = 1
    for _ in range(q):
        cases.append((data[pos].decode(), data[pos + 1].decode()))
        pos += 2
    return cases


# --- clause: can_type :: (s: str, t: str) -> bool ---
def can_type(s, t):
    j = len(t) - 1
    i = len(s) - 1
    while j >= 0:
        if i < 0:
            return False
        if s[i] == t[j]:
            j -= 1
            i -= 1
        else:
            i -= 2
    return True


# --- clause: main :: () -> None ---
def main():
    out = []
    for s, t in read_input():
        out.append("YES" if can_type(s, t) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
