import sys


# --- clause: read_input :: () -> list[tuple[int, int, str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    offset = 1
    cases = []
    for _ in range(t):
        n = int(fields[offset])
        a = int(fields[offset + 1])
        offset += 3
        cases.append((n, a, fields[offset].decode()))
        offset += 1
    return cases


# --- clause: verdict :: (n: int, a: int, notes: str) -> str ---
def verdict(n, a, notes):
    online = a
    reached = a == n
    known = a
    for ch in notes:
        if ch == "+":
            online += 1
            known += 1
        else:
            online -= 1
        if online == n:
            reached = True
    if reached:
        return "YES"
    return "MAYBE" if known >= n else "NO"


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, a, notes in read_input():
        out.append(verdict(n, a, notes))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
