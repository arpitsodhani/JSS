import sys


# --- clause: read_input :: () -> str ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return fields[1].decode()


# --- clause: smallest_form :: (s: str) -> str ---
def smallest_form(s):
    zeros = 0
    ones = 0
    for ch in s:
        if ch == "0":
            zeros += 1
        else:
            ones += 1
    if ones == 0:
        return "0"
    return "1" + "0" * zeros


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(smallest_form(read_input()) + "\n")


if __name__ == "__main__":
    main()
