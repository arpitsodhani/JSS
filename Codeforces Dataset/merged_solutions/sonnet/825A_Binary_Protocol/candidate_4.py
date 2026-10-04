import sys


# --- clause: read_input :: () -> str ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[1].decode()


# --- clause: decode :: (s: str) -> str ---
def decode(s):
    digits = []
    for chunk in s.split("0"):
        digits.append(str(len(chunk)))
    return "".join(digits)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(decode(read_input()) + "\n")


if __name__ == "__main__":
    main()
