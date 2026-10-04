import sys


# --- clause: read_input :: () -> list[tuple[int, int, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cursor = 1
    cases = []
    for _ in range(t):
        n = int(numbers[cursor])
        a = int(numbers[cursor + 1])
        cursor += 3
        cases.append((n, a, numbers[cursor].decode()))
        cursor += 1
    return cases


# --- clause: verdict :: (n: int, a: int, notes: str) -> str ---
def verdict(n, a, notes):
    joins = 0
    for ch in notes:
        if ch == "+":
            joins += 1
    online = a
    peak = a
    for ch in notes:
        online += 1 if ch == "+" else -1
        if online > peak:
            peak = online
    if peak >= n:
        return "YES"
    return "MAYBE" if a + joins >= n else "NO"


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, a, notes in read_input():
        out.append(verdict(n, a, notes))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
