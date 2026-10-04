import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: build_array :: (n: int) -> list[int] ---
def build_array(n):
    pieces = []
    for value in range(n, 0, -1):
        pieces.append(value)
    pieces.append(n)
    for value in range(1, n):
        pieces.append(value)
    return pieces


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for n in read_input():
        pieces.append(" ".join(map(str, build_array(n))))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
