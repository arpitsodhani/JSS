import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: build_word :: (n: int) -> str ---
def build_word(n):
    vowels = "aeiou"
    letters = []
    for i in range(n):
        letters.append(vowels[i % 5])
    letters.sort()
    return "".join(letters)


# --- clause: main :: () -> None ---
def main():
    collected = []
    for n in read_input():
        collected.append(build_word(n))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
