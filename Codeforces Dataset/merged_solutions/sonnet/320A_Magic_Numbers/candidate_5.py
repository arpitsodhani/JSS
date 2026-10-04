import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: is_magic :: (digits: str) -> bool ---
def is_magic(digits):
    position = 0
    size = len(digits)
    while position < size:
        if digits[position] != "1":
            return False
        position += 1
        stop = position
        while stop < size and digits[stop] == "4":
            stop += 1
        if stop - position > 2:
            return False
        position = stop
    return True


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("YES\n" if is_magic(read_input()) else "NO\n")


if __name__ == "__main__":
    main()
