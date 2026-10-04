import sys


# --- clause: read_input :: () -> list[tuple[int, int, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        a = int(data[pos + 1])
        pos += 3
        cases.append((n, a, data[pos].decode()))
        pos += 1
    return cases


# --- clause: verdict :: (n: int, a: int, notes: str) -> str ---
def verdict(n, a, notes):
    online = a
    reached = a == n
    seen = a
    for ch in notes:
        if ch == "+":
            online += 1
            seen += 1
        else:
            online -= 1
        if online == n:
            reached = True
    if reached:
        return "YES"
    return "MAYBE" if seen >= n else "NO"


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, a, notes in read_input():
        out.append(verdict(n, a, notes))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
