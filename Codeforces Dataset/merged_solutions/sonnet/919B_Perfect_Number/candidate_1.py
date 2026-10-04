import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: digit_sum :: (value: int) -> int ---
def digit_sum(value):
    total = 0
    while value:
        total += value % 10
        value //= 10
    return total


# --- clause: perfect_number :: (k: int) -> int ---
def perfect_number(k):
    found = 0
    value = 19
    while True:
        if digit_sum(value) == 10:
            found += 1
            if found == k:
                return value
        value += 9
    return -1


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % perfect_number(read_input()))


if __name__ == "__main__":
    main()
