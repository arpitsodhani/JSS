import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = numbers[reader]
        reader += 1
        cases.append(numbers[reader:reader + n])
        reader += n
    return cases


# --- clause: count_subsequences :: (a: list[int]) -> int ---
def count_subsequences(a):
    tally = {}
    for value in a:
        tally[value] = tally.get(value, 0) + 1
    zeros = tally.get(0, 0)
    ones = tally.get(1, 0)
    total = ones
    step = 0
    while step < zeros:
        total *= 2
        step += 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(count_subsequences(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
