import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: count_multiples :: (s: str) -> int ---
def count_multiples(s):
    total = 0
    n = len(s)
    for i in range(n):
        digit = int(s[i])
        if digit % 4 == 0:
            total += 1
        if i > 0 and int(s[i - 1:i + 1]) % 4 == 0:
            total += i
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(count_multiples(read_input())) + "\n")


if __name__ == "__main__":
    main()
