import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# --- clause: wait_time :: (year: int) -> int ---
def wait_time(year):
    digits = str(year)
    lead = int(digits[0]) + 1
    nxt = lead * 10 ** (len(digits) - 1)
    return nxt - year

# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(wait_time(read_input())) + "\n")


if __name__ == "__main__":
    main()
