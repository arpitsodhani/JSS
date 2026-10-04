import sys


# --- clause: read_input :: () -> list[tuple[int, int, str]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    reader = 1
    cases = []
    for _ in range(t):
        n = int(raw[reader])
        a = int(raw[reader + 1])
        reader += 3
        cases.append((n, a, raw[reader].decode()))
        reader += 1
    return cases


# --- clause: verdict :: (n: int, a: int, notes: str) -> str ---
def verdict(n, a, notes):
    online = a
    reached = a == n
    visited = a
    for ch in notes:
        if ch == "+":
            online += 1
            visited += 1
        else:
            online -= 1
        if online == n:
            reached = True
    if reached:
        return "YES"
    return "MAYBE" if visited >= n else "NO"


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, a, notes in read_input():
        out.append(verdict(n, a, notes))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
