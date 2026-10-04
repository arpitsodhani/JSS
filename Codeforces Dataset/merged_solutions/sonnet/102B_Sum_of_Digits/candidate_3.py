import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    text = data[0].decode()
    return text


# --- clause: spell_count :: (digits: str) -> int ---
def spell_count(digits):
    steps = 0
    value = digits
    while True:
        if len(value) <= 1:
            return steps
        total = 0
        index = 0
        while index < len(value):
            total += ord(value[index]) - 48
            index += 1
        value = str(total)
        steps += 1


# --- clause: main :: () -> None ---
def main():
    print(spell_count(read_input()))


if __name__ == "__main__":
    main()
