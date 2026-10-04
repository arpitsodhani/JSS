import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# --- clause: wait_time :: (year: int) -> int ---
def wait_time(year):
    scale = 1
    lead = year
    while lead >= 10:
        lead //= 10
        scale *= 10
    return (lead + 1) * scale - year

# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(wait_time(read_input())) + "\n")


if __name__ == "__main__":
    main()
