import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    cases = []
    for i in range(t):
        cases.append((tokens[1 + 2 * i], tokens[2 + 2 * i]))
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
    lines = []
    for x, y in read_input():
        lines.append("YES" if can_reach(x, y) else "NO")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
