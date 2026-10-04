import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    values = list(map(int, sys.stdin.buffer.read().split()))
    total = values[0]
    target = values[1]
    portals = values[2:2 + total - 1]
    return total, target, portals


# --- clause: can_reach :: (n: int, t: int, jumps: list[int]) -> bool ---
def can_reach(n, t, jumps):
    pos = 1
    while pos < t:
        step = jumps[pos - 1]
        pos = pos + step
    return pos == t


# --- clause: main :: () -> None ---
def main():
    total, target, portals = read_input()
    reached = can_reach(total, target, portals)
    sys.stdout.write(("YES" if reached else "NO") + "\n")


if __name__ == "__main__":
    main()
