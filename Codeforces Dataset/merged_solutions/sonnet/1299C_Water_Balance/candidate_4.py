import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: flatten :: (a: list[int]) -> list[tuple[int, int]] ---
def flatten(a):
    totals = []
    widths = []
    for value in a:
        totals.append(value)
        widths.append(1)
        while len(totals) > 1 and totals[-2] * widths[-1] >= totals[-1] * widths[-2]:
            total = totals.pop() + totals[-1]
            width = widths.pop() + widths[-1]
            totals[-1] = total
            widths[-1] = width
    return [(totals[i], widths[i]) for i in range(len(totals))]


# --- clause: main :: () -> None ---
def main():
    out = []
    for total, width in flatten(read_input()):
        value = "%.9f" % (total / width)
        for _ in range(width):
            out.append(value)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
