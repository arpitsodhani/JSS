import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: paint_stones :: (n: int, strengths: list[int]) -> tuple[int, str] ---
def paint_stones(n, strengths):
    half = n // 2
    zeros = sum(1 for value in strengths if value % 3 == 0)
    if zeros <= half:
        pick_zero = True
        coefficient = 0
    else:
        pick_zero = False
        coefficient = 2
    colour = ["1"] * n
    left = half
    for index, value in enumerate(strengths):
        if left == 0:
            break
        matches = (value % 3 == 0) == pick_zero
        if matches:
            colour[index] = "0"
            left -= 1
    for index in range(n):
        if left == 0:
            break
        if colour[index] == "1":
            colour[index] = "0"
            left -= 1
    return coefficient, "".join(colour)


# --- clause: main :: () -> None ---
def main():
    n, strengths = read_input()
    coefficient, colour = paint_stones(n, strengths)
    sys.stdout.write(str(coefficient) + "\n" + colour + "\n")


if __name__ == "__main__":
    main()
