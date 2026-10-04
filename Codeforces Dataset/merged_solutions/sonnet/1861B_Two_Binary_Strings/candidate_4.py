import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i].decode(), numbers[2 + 2 * i].decode()))
    return cases


# --- clause: can_match :: (a: str, b: str) -> bool ---
def can_match(a, b):
    spots = set()
    for i in range(len(a) - 1):
        if a[i] == "0" and a[i + 1] == "1":
            spots.add(i)
    for i in range(len(b) - 1):
        if b[i] == "0" and b[i + 1] == "1" and i in spots:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for a, b in read_input():
        pieces.append("YES" if can_match(a, b) else "NO")
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
