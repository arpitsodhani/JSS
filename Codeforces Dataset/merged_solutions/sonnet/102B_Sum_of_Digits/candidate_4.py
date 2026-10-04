import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return bytes(data[0]).decode()


# --- clause: spell_count :: (digits: str) -> int ---
def spell_count(digits):
    steps = 0
    while len(digits) > 1:
        total = 0
        for ch in digits:
            total = total + int(ch)
        digits = "%d" % total
        steps += 1
    return steps


# --- clause: main :: () -> None ---
def main():
    digits = read_input()
    sys.stdout.write(str(spell_count(digits)) + "\n")


if __name__ == "__main__":
    main()
