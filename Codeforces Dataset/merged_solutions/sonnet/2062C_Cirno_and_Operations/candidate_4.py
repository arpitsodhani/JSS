import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    cursor = 0
    tests = nums[cursor]
    cursor += 1
    cases = []
    while len(cases) < tests:
        n = nums[cursor]
        cursor += 1
        cases.append(nums[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: solve_case :: (a: list[int]) -> int ---
def solve_case(a):
    cur = list(a)
    best = sum(cur)
    while len(cur) > 1:
        diffs = []
        for i in range(len(cur) - 1):
            diffs.append(cur[i + 1] - cur[i])
        cur = diffs
        value = sum(cur)
        value = -value if value < 0 else value
        best = max(best, value)
    return best


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    result = []
    for i in range(len(cases)):
        result.append(str(solve_case(cases[i])))
    print("\n".join(result))


if __name__ == "__main__":
    main()
