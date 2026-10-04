import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int], list[int]]] ---
def read_input():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    cursor = 0
    cases_count = nums[cursor]
    cursor += 1
    cases = []
    while len(cases) < cases_count:
        n = nums[cursor]
        cursor += 1
        father = [0] * (n + 1)
        for v in range(2, n + 1):
            father[v] = nums[cursor]
            cursor += 1
        l = [0] * (n + 1)
        r = [0] * (n + 1)
        for v in range(1, n + 1):
            l[v] = nums[cursor]
            r[v] = nums[cursor + 1]
            cursor += 2
        cases.append((n, father, l, r))
    return cases


# --- clause: solve_case :: (n: int, parent: list[int], low: list[int], high: list[int]) -> int ---
def solve_case(n, parent, low, high):
    received = [0] * (n + 2)
    moves = 0
    for v in range(n, 0, -1):
        amount = received[v]
        if amount < low[v]:
            moves += 1
            amount = high[v]
        elif amount > high[v]:
            amount = high[v]
        received[parent[v]] += amount
    return moves


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    result = []
    for i in range(len(cases)):
        n, father, l, r = cases[i]
        result.append(str(solve_case(n, father, l, r)))
    print("\n".join(result))


if __name__ == "__main__":
    main()
