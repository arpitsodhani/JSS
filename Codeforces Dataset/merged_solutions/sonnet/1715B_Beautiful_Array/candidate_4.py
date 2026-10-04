import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    cases = []
    cursor = 1
    for _ in range(nums[0]):
        cases.append(tuple(nums[cursor:cursor + 4]))
        cursor += 4
    return cases


# --- clause: solve_case :: (n: int, k: int, b: int, s: int) -> str ---
def solve_case(n, k, b, s):
    base = k * b
    top = base + n * (k - 1)
    if s < base or top < s:
        return "-1"
    a = [0] * n
    anchor = min(s, base + k - 1)
    a[0] = anchor
    leftover = s - anchor
    for i in range(1, n):
        chunk = min(leftover, k - 1)
        a[i] = chunk
        leftover -= chunk
    return " ".join(map(str, a))


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    out = []
    for i in range(len(cases)):
        n, k, b, s = cases[i]
        out.append(solve_case(n, k, b, s))
    print("\n".join(out))


if __name__ == "__main__":
    main()
