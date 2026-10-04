import sys


# --- clause: read_input :: () -> str ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[1].decode()


# --- clause: nearly_correct :: (s: str) -> bool ---
def nearly_correct(s):
    opens = s.count("(")
    if opens * 2 != len(s):
        return False
    depth = 0
    dips = 0
    for ch in s:
        if ch == "(":
            depth += 1
        else:
            depth -= 1
            if depth < 0:
                dips += 1
                depth = 0
    return dips <= 1


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("Yes\n" if nearly_correct(read_input()) else "No\n")


if __name__ == "__main__":
    main()
