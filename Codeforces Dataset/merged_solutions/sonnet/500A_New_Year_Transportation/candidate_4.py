import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    cells = raw[0]
    goal = raw[1]
    steps = raw[2:cells + 1]
    return cells, goal, steps


# --- clause: can_reach :: (n: int, t: int, jumps: list[int]) -> bool ---
def can_reach(n, t, jumps):
    current = 1
    while current < t:
        current = current + jumps[current - 1]
    return t == current


# --- clause: main :: () -> None ---
def main():
    params = read_input()
    ok = can_reach(params[0], params[1], params[2])
    print("YES" if ok else "NO")


if __name__ == "__main__":
    main()
