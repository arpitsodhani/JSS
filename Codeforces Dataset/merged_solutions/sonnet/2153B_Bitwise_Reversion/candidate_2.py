import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 3 * i], tokens[2 + 3 * i], tokens[3 + 3 * i]))
    return cases


# --- clause: can_build :: (x: int, y: int, z: int) -> bool ---
def can_build(x, y, z):
    for bit in range(30):
        ones = ((x >> bit) & 1) + ((y >> bit) & 1) + ((z >> bit) & 1)
        if ones == 2:
            return False
    return True


# --- clause: main :: () -> None ---
def main():
    lines = []
    for x, y, z in read_input():
        lines.append("YES" if can_build(x, y, z) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
