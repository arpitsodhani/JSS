import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: paint_stones :: (n: int, strengths: list[int]) -> tuple[int, str] ---
def paint_stones(n, strengths):
    divisible = []
    rest = []
    for index, value in enumerate(strengths):
        if value % 3:
            rest.append(index)
        else:
            divisible.append(index)
    half = n // 2
    if len(divisible) <= half:
        first = divisible
        filler = rest
        coefficient = 0
    else:
        first = rest
        filler = divisible
        coefficient = 2
    colour = ["1"] * n
    for index in first:
        colour[index] = "0"
    need = half - len(first)
    for index in filler[:need]:
        colour[index] = "0"
    return coefficient, "".join(colour)


# --- clause: main :: () -> None ---
def main():
    n, strengths = read_input()
    coefficient, colour = paint_stones(n, strengths)
    sys.stdout.write(str(coefficient) + "\n" + colour + "\n")


if __name__ == "__main__":
    main()
