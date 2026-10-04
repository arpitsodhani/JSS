import sys


# --- clause: read_input :: () -> str ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return raw[1].decode()


# --- clause: is_maximal :: (row: str) -> bool ---
def is_maximal(row):
    n = len(row)
    for i in range(n):
        if row[i] == "1":
            if i > 0 and row[i - 1] == "1":
                return False
            if i + 1 < n and row[i + 1] == "1":
                return False
        else:
            free = True
            if i > 0 and row[i - 1] == "1":
                free = False
            if i + 1 < n and row[i + 1] == "1":
                free = False
            if free:
                return False
    return True


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("Yes\n" if is_maximal(read_input()) else "No\n")


if __name__ == "__main__":
    main()
