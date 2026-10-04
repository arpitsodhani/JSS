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


# --- clause: solve_case :: (p: list[int]) -> int ---
def solve_case(p):
    n = len(p)
    at = [0] * (n + 2)
    for i in range(1, n + 1):
        at[p[i - 1]] = i
    best = 0
    done = 0
    open_marks = 0
    for h in range(1, n + 2):
        if h > 1:
            value = p[h - 2]
            if value <= h - 1:
                done += 1
            if at[h - 1] < h - 1:
                open_marks -= 1
            if value >= h:
                open_marks += 1
        if best < done + open_marks:
            best = done + open_marks
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
