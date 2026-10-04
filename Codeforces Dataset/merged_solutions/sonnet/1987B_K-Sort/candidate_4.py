import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: coins_needed :: (a: list[int]) -> int ---
def coins_needed(a):
    gaps = []
    peak = a[0]
    for value in a:
        if value > peak:
            peak = value
        gaps.append(peak - value)
    return sum(gaps) + max(gaps)


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(coins_needed(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
