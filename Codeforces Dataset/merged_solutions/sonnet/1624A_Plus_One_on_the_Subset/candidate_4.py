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


# --- clause: steps_needed :: (a: list[int]) -> int ---
def steps_needed(a):
    low = a[0]
    high = a[0]
    for value in a:
        if value < low:
            low = value
        if value > high:
            high = value
    return high - low


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(steps_needed(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
