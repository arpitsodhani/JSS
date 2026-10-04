import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return str(data[0], "ascii")


# --- clause: spell_count :: (digits: str) -> int ---
def spell_count(digits):
    steps = 0
    while len(digits) > 1:
        digits = str(sum(int(ch) for ch in digits))
        steps += 1
    return steps


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % spell_count(read_input()))


if __name__ == "__main__":
    main()
