import sys


# --- clause: read_input :: () -> list[tuple[int, str, str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    cases = []
    offset = 1
    for _ in range(t):
        n = int(fields[offset])
        k = int(fields[offset + 1])
        cases.append((k, fields[offset + 2].decode(), fields[offset + 3].decode()))
        offset += 4
    return cases


# --- clause: can_change :: (k: int, s: str, t: str) -> bool ---
def can_change(k, s, t):
    n = len(s)
    loose = []
    for i in range(n):
        if i + k < n or i - k >= 0:
            loose.append(i)
        elif s[i] != t[i]:
            return False
    start = sorted(s[i] for i in loose)
    right = sorted(t[i] for i in loose)
    return start == right


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, s, t in read_input():
        out.append("YES" if can_change(k, s, t) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
