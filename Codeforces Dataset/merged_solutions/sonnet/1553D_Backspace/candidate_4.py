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
    n = len(s)
    m = len(t)
    i = n - 1
    j = m - 1
    while j >= 0 and i >= 0:
        if s[i] != t[j]:
            i -= 2
            continue
        i -= 1
        j -= 1
    return j == -1


# --- clause: main :: () -> None ---
def main():
    out = []
    for s, t in read_input():
        out.append("YES" if can_type(s, t) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
