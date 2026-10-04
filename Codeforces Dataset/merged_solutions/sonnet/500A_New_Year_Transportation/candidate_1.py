import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    t = data[1]
    jumps = data[2:1 + n]
    return n, t, jumps


# --- clause: can_reach :: (n: int, t: int, jumps: list[int]) -> bool ---
def can_reach(n, t, jumps):
    cell = 1
    while cell < t:
        cell += jumps[cell - 1]
    return cell == t


# --- clause: main :: () -> None ---
def main():
    n, t, jumps = read_input()
    print("YES" if can_reach(n, t, jumps) else "NO")


if __name__ == "__main__":
    main()
