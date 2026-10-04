import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: is_leap :: (year: int) -> bool ---
def is_leap(year):
    if year % 400 == 0:
        return True
    return year % 4 == 0 and year % 100 != 0


# --- clause: next_same :: (year: int) -> int ---
def next_same(year):
    shift = 0
    delta = year
    while True:
        shift = (shift + (366 if is_leap(delta) else 365)) % 7
        delta += 1
        if shift == 0 and is_leap(delta) == is_leap(year):
            return delta


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % next_same(read_input()))


if __name__ == "__main__":
    main()
