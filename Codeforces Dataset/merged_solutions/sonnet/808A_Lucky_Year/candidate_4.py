import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# --- clause: wait_time :: (year: int) -> int ---
def wait_time(year):
    scale = 1
    while scale * 10 <= year:
        scale *= 10
    top = year // scale
    return (top + 1) * scale - year

# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(wait_time(read_input())) + "\n")


if __name__ == "__main__":
    main()
