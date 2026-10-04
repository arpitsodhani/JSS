import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: build_word :: (n: int) -> str ---
def build_word(n):
    vowels = "aeiou"
    pieces = []
    for i in range(5):
        times = n // 5 + (1 if i < n % 5 else 0)
        pieces.append(vowels[i] * times)
    return "".join(pieces)


# --- clause: main :: () -> None ---
def main():
    written = []
    for n in read_input():
        written.append(build_word(n))
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
