import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 3 * i], numbers[2 + 3 * i], numbers[3 + 3 * i]))
    return cases


# --- clause: can_build :: (x: int, y: int, z: int) -> bool ---
def can_build(x, y, z):
    a = x | z
    b = x | y
    c = y | z
    return a & b == x and b & c == y and a & c == z


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for x, y, z in read_input():
        pieces.append("YES" if can_build(x, y, z) else "NO")
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
