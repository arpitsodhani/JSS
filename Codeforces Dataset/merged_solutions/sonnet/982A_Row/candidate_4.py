import sys


# --- clause: read_input :: () -> str ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[1].decode()


# --- clause: is_maximal :: (row: str) -> bool ---
def is_maximal(row):
    if "11" in row:
        return False
    padded = "0" + row + "0"
    if "000" in padded:
        return False
    return True


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("Yes\n" if is_maximal(read_input()) else "No\n")


if __name__ == "__main__":
    main()
