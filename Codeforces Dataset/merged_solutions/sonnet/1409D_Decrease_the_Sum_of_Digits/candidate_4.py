import sys


# --- clause: read_input :: () -> list[tuple[int, int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cases = []
    for i in range(t):
        cases.append((numbers[1 + 2 * i], numbers[2 + 2 * i]))
    return cases


# --- clause: digit_sum :: (n: int) -> int ---
def digit_sum(n):
    summed = 0
    while n:
        summed += n % 10
        n //= 10
    return summed


# --- clause: moves_needed :: (n: int, s: int) -> int ---
def moves_needed(n, s):
    power = 1
    value = n
    while digit_sum(value) > s:
        power *= 10
        value = (n // power + 1) * power
    return value - n


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, s in read_input():
        out.append(moves_needed(n, s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
