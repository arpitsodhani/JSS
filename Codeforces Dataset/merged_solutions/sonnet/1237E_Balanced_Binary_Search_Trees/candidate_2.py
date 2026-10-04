import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# --- clause: build_valid :: (limit: int) -> set[int] ---
def build_valid(limit):
    valid = set()
    for seed, offset in ((1, 5), (2, 2), (4, 4), (5, 1)):
        value = seed
        while value <= limit:
            valid.add(value)
            value = 4 * value + offset
    return valid

# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("1\n" if n in build_valid(n) else "0\n")


if __name__ == "__main__":
    main()
