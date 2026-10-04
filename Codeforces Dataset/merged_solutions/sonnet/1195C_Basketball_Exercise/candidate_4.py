import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    return numbers[1:1 + n], numbers[1 + n:1 + 2 * n]


# --- clause: best_team :: (top: list[int], low: list[int]) -> int ---
def best_team(top, low):
    n = len(top)
    first = [0] * (n + 1)
    second = [0] * (n + 1)
    for i in range(n):
        first[i + 1] = second[i] + top[i]
        if first[i] > first[i + 1]:
            first[i + 1] = first[i]
        second[i + 1] = first[i] + low[i]
        if second[i] > second[i + 1]:
            second[i + 1] = second[i]
    return first[n] if first[n] > second[n] else second[n]


# --- clause: main :: () -> None ---
def main():
    top, low = read_input()
    sys.stdout.write("%d\n" % best_team(top, low))


if __name__ == "__main__":
    main()
