import sys


# --- clause: read_input :: () -> list[tuple[str, str, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 3 * i].decode(), numbers[2 + 3 * i].decode(), numbers[3 + 3 * i].decode()))
    return cases


# --- clause: can_match :: (a: str, b: str, c: str) -> bool ---
def can_match(a, b, c):
    for i in range(len(c)):
        if c[i] != a[i] and c[i] != b[i]:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for a, b, c in read_input():
        pieces.append("YES" if can_match(a, b, c) else "NO")
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
