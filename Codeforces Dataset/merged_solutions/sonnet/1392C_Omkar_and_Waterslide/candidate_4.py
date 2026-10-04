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


# --- clause: raise_count :: (a: list[int]) -> int ---
def raise_count(a):
    total = 0
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            total += a[i - 1] - a[i]
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(raise_count(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
