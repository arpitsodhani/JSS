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


# --- clause: candies_eaten :: (a: list[int]) -> int ---
def candies_eaten(a):
    low = a[0]
    total = 0
    for value in a:
        if value < low:
            low = value
        total += value
    return total - low * len(a)


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(candies_eaten(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
