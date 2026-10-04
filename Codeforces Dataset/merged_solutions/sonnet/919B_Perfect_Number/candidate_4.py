import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: digit_sum :: (value: int) -> int ---
def digit_sum(value):
    summed = 0
    while value:
        summed += value % 10
        value //= 10
    return summed


# --- clause: perfect_number :: (k: int) -> int ---
def perfect_number(k):
    found = 0
    value = 18
    while found < k:
        value += 1
        if digit_sum(value) == 10:
            found += 1
    return value


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % perfect_number(read_input()))


if __name__ == "__main__":
    main()
