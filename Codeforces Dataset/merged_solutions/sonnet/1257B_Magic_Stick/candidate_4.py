import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return cases


# --- clause: can_reach :: (x: int, y: int) -> bool ---
def can_reach(x, y):
    if x >= 4:
        return True
    if x == 1:
        return y == 1
    return y <= 3


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for x, y in read_input():
        pieces.append("YES" if can_reach(x, y) else "NO")
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
