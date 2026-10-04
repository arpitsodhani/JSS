import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: count_multiples :: (s: str) -> int ---
def count_multiples(s):
    total = 0
    n = len(s)
    i = 0
    while i < n:
        digit = ord(s[i]) - 48
        if digit % 4 == 0:
            total += 1
        if i:
            two = (ord(s[i - 1]) - 48) * 10 + digit
            if two % 4 == 0:
                total += i
        i += 1
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(count_multiples(read_input())) + "\n")


if __name__ == "__main__":
    main()
