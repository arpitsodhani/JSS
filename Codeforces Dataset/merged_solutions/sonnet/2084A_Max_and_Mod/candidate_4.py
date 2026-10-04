import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    total = nums[0]
    return [nums[idx + 1] for idx in range(total)]


# --- clause: solve_case :: (n: int) -> str ---
def solve_case(n):
    if n % 2:
        perm = [n] + [v for v in range(1, n)]
        return " ".join(map(str, perm))
    return "-1"


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    lines = []
    for i in range(len(cases)):
        lines.append(solve_case(cases[i]))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
