import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    return n, k, numbers[2:2 + n], numbers[2 + n:2 + 2 * n]


# --- clause: apply_step :: (goes: list[int], sums: list[int], lows: list[int], step_goes: list[int], step_sums: list[int], step_lows: list[int]) -> None ---
def apply_step(goes, sums, lows, step_goes, step_sums, step_lows):
    for i in range(len(goes)):
        j = goes[i]
        sums[i] += step_sums[j]
        if step_lows[j] < lows[i]:
            lows[i] = step_lows[j]
        goes[i] = step_goes[j]


# --- clause: double_step :: (step_goes: list[int], step_sums: list[int], step_lows: list[int]) -> tuple[list[int], list[int], list[int]] ---
def double_step(step_goes, step_sums, step_lows):
    n = len(step_goes)
    goes = [0] * n
    sums = [0] * n
    lows = [0] * n
    for i in range(n):
        j = step_goes[i]
        goes[i] = step_goes[j]
        sums[i] = step_sums[i] + step_sums[j]
        lows[i] = step_lows[i] if step_lows[i] < step_lows[j] else step_lows[j]
    return goes, sums, lows


# --- clause: walk_paths :: (n: int, k: int, f: list[int], w: list[int]) -> tuple[list[int], list[int]] ---
def walk_paths(n, k, f, w):
    goes = list(range(n))
    sums = [0] * n
    lows = [1 << 62] * n
    step_goes = f
    step_sums = w
    step_lows = w
    while k:
        if k & 1:
            apply_step(goes, sums, lows, step_goes, step_sums, step_lows)
        k >>= 1
        if k:
            step_goes, step_sums, step_lows = double_step(step_goes, step_sums, step_lows)
    return sums, lows


# --- clause: main :: () -> None ---
def main():
    n, k, f, w = read_input()
    sums, lows = walk_paths(n, k, f, w)
    pieces = []
    for i in range(n):
        pieces.append("%d %d" % (sums[i], lows[i]))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
