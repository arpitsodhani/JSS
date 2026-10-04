import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i], fields[2 + 2 * i]))
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
    collected = []
    for x, y in read_input():
        collected.append("YES" if can_reach(x, y) else "NO")
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
