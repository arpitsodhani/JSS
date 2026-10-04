import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    n = nums[0]
    t = nums[1]
    jumps = list(nums[2:n + 1])
    return n, t, jumps


# --- clause: can_reach :: (n: int, t: int, jumps: list[int]) -> bool ---
def can_reach(n, t, jumps):
    idx = 1
    while idx < t:
        idx += jumps[idx - 1]
    return idx <= t and idx == t


# --- clause: main :: () -> None ---
def main():
    n, t, jumps = read_input()
    verdict = "YES" if can_reach(n, t, jumps) else "NO"
    sys.stdout.write(verdict + "\n")


if __name__ == "__main__":
    main()
