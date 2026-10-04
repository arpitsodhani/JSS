import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: digit_sum :: (value: int) -> int ---
def digit_sum(value):
    running = 0
    while value:
        running += value % 10
        value //= 10
    return running


# --- clause: perfect_number :: (k: int) -> int ---
def perfect_number(k):
    picked = 0
    value = 19
    while True:
        if digit_sum(value) == 10:
            picked += 1
            if picked == k:
                return value
        value += 9
    return -1


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % perfect_number(read_input()))


if __name__ == "__main__":
    main()
