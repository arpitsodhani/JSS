import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cursor = 1
    cases = []
    for _ in range(t):
        c0 = int(numbers[cursor + 1])
        c1 = int(numbers[cursor + 2])
        h = int(numbers[cursor + 3])
        s = numbers[cursor + 4].decode()
        cursor += 5
        cases.append((c0, c1, h, s))
    return cases


# --- clause: least_price :: (c0: int, c1: int, h: int, s: str) -> int ---
def least_price(c0, c1, h, s):
    ones = s.count("1")
    zeros = len(s) - ones
    plain = zeros * c0 + ones * c1
    all_zero = len(s) * c0 + ones * h
    all_one = len(s) * c1 + zeros * h
    total = plain
    if all_zero < total:
        total = all_zero
    if all_one < total:
        total = all_one
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for c0, c1, h, s in read_input():
        out.append(least_price(c0, c1, h, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
