import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: count_good :: (a: list[int]) -> int ---
def count_good(a):
    n = len(a)
    odds = [element for element in a if element % 2]
    evens = n - len(odds)
    total = 0
    for k in range(evens):
        total += n - 1 - k
    for i in range(len(odds)):
        for j in range(i + 1, len(odds)):
            if gcd_of(odds[i], odds[j]) > 1:
                total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(count_good(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
