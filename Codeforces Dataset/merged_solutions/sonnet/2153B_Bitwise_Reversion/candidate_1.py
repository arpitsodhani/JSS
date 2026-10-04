import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    for i in range(t):
        cases.append((data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]))
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
    out = []
    for x, y, z in read_input():
        out.append("YES" if can_build(x, y, z) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
