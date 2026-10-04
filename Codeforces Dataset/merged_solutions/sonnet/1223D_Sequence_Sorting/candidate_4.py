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
    first_at = {}
    last_at = {}
    for i in range(len(a) - 1, -1, -1):
        v = a[i]
        if v not in last_at:
            last_at[v] = i
        first_at[v] = i
    distinct = sorted(first_at)
    best = 1
    streak = 1
    for j in range(1, len(distinct)):
        if last_at[distinct[j - 1]] < first_at[distinct[j]]:
            streak += 1
        else:
            streak = 1
        best = max(best, streak)
    return len(distinct) - best


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    result = []
    for i in range(len(cases)):
        result.append(str(solve_case(cases[i])))
    print("\n".join(result))


if __name__ == "__main__":
    main()
