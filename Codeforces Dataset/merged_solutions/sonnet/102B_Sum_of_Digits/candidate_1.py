import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode()


# --- clause: spell_count :: (digits: str) -> int ---
def spell_count(digits):
    steps = 0
    while len(digits) > 1:
        total = 0
        for ch in digits:
            total += ord(ch) - 48
        digits = str(total)
        steps += 1
    return steps


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(str(spell_count(read_input())) + "\n")


if __name__ == "__main__":
    main()
