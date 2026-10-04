import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    t = int(tokens[1])
    jumps = [int(x) for x in tokens[2:1 + n]]
    return n, t, jumps


# --- clause: can_reach :: (n: int, t: int, jumps: list[int]) -> bool ---
def can_reach(n, t, jumps):
    here = 1
    while here < t:
        here += jumps[here - 1]
    if here == t:
        return True
    return False


# --- clause: main :: () -> None ---
def main():
    n, t, jumps = read_input()
    answer = "YES" if can_reach(n, t, jumps) else "NO"
    print(answer)


if __name__ == "__main__":
    main()
