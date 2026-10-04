import sys


# --- clause: read_input :: () -> int ---
def read_input():
    return int(sys.stdin.buffer.read().split()[0])


# --- clause: build_valid :: (limit: int) -> set[int] ---
def build_valid(limit):
    valid = set()
    low = 1
    high = 2
    phase = 0
    while low <= limit:
        valid.add(low)
        valid.add(high)
        if phase == 0:
            low, high = 2 * low + 2, 2 * high + 1
        else:
            low, high = 2 * low + 1, 2 * high
        phase ^= 1
    return valid


# --- clause: main :: () -> None ---
def main():
    n = read_input()
    sys.stdout.write("1\n" if n in build_valid(n) else "0\n")


if __name__ == "__main__":
    main()
