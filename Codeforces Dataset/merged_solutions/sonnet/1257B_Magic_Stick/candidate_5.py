import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    cases = []
    for i in range(t):
        cases.append((raw[1 + 2 * i], raw[2 + 2 * i]))
    return cases


# --- clause: can_reach :: (x: int, y: int) -> bool ---
def can_reach(x, y):
    if y <= x:
        return True
    if x == 1:
        return False
    if x >= 4:
        return True
    return y <= 3


# --- clause: main :: () -> None ---
def main():
    written = []
    for x, y in read_input():
        written.append("YES" if can_reach(x, y) else "NO")
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
