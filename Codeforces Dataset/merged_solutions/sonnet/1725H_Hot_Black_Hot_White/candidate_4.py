import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: paint_stones :: (n: int, strengths: list[int]) -> tuple[int, str] ---
def paint_stones(n, strengths):
    half = n // 2
    zeros = [i for i, value in enumerate(strengths) if value % 3 == 0]
    if len(zeros) <= half:
        group = set(zeros)
        coefficient = 0
    else:
        group = set(i for i in range(n) if strengths[i] % 3)
        coefficient = 2
    for index in range(n):
        if len(group) == half:
            break
        if index not in group:
            group.add(index)
    colour = []
    for index in range(n):
        colour.append("0" if index in group else "1")
    return coefficient, "".join(colour)


# --- clause: main :: () -> None ---
def main():
    n, strengths = read_input()
    coefficient, colour = paint_stones(n, strengths)
    sys.stdout.write(str(coefficient) + "\n" + colour + "\n")


if __name__ == "__main__":
    main()
