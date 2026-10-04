import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: count_multiples :: (s: str) -> int ---
def count_multiples(s):
    total = 0
    for i, ch in enumerate(s):
        if (ord(ch) - 48) % 4 == 0:
            total += 1
        if i:
            pair = (ord(s[i - 1]) - 48) * 10 + ord(ch) - 48
            if pair % 4 == 0:
                total += i
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(count_multiples(read_input())) + "\n")


if __name__ == "__main__":
    main()
