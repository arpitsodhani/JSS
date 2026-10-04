import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: count_multiples :: (s: str) -> int ---
def count_multiples(s):
    total = 0
    previous = -1
    for index, ch in enumerate(s):
        digit = ord(ch) - 48
        if digit % 4 == 0:
            total += 1
        if previous >= 0 and (previous * 10 + digit) % 4 == 0:
            total += index
        previous = digit
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(count_multiples(read_input())) + "\n")


if __name__ == "__main__":
    main()
