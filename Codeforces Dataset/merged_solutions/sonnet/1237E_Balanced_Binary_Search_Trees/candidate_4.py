import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# --- clause: build_valid :: (limit: int) -> set[int] ---
def build_valid(limit):
    valid = set()
    low = 1
    high = 2
    even_step = True
    while low <= limit:
        valid.add(low)
        valid.add(high)
        if even_step:
            low = 2 * low + 2
            high = 2 * high + 1
        else:
            low = 2 * low + 1
            high = 2 * high
        even_step = not even_step
    return valid

# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("1\n" if n in build_valid(n) else "0\n")


if __name__ == "__main__":
    main()
