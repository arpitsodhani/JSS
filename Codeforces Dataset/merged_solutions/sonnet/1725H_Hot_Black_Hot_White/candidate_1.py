import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: paint_stones :: (n: int, strengths: list[int]) -> tuple[int, str] ---
def paint_stones(n, strengths):
    zeros = [i for i in range(n) if strengths[i] % 3 == 0]
    others = [i for i in range(n) if strengths[i] % 3]
    half = n // 2
    colour = ["1"] * n
    if len(zeros) <= half:
        chosen = zeros + others[:half - len(zeros)]
        coefficient = 0
    else:
        chosen = others + zeros[:half - len(others)]
        coefficient = 2
    for index in chosen:
        colour[index] = "0"
    return coefficient, "".join(colour)


# --- clause: main :: () -> None ---
def main():
    n, strengths = read_input()
    coefficient, colour = paint_stones(n, strengths)
    sys.stdout.write(str(coefficient) + "\n" + colour + "\n")


if __name__ == "__main__":
    main()
