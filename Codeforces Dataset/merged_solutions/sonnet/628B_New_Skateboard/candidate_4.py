import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: count_multiples :: (s: str) -> int ---
def count_multiples(s):
    digits = [ord(ch) - 48 for ch in s]
    total = sum(1 for d in digits if d % 4 == 0)
    for i in range(1, len(digits)):
        if (digits[i - 1] * 10 + digits[i]) % 4 == 0:
            total += i
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(count_multiples(read_input())) + "\n")


if __name__ == "__main__":
    main()
