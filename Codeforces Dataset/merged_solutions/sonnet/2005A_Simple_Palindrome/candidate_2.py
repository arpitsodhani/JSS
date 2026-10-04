import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


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
    lines = []
    for n in read_input():
        lines.append(build_word(n))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
