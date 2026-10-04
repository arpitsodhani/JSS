import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: flatten :: (a: list[int]) -> list[tuple[int, int]] ---
def flatten(a):
    stack = []
    for value in a:
        summed = value
        width = 1
        while stack and stack[-1][0] * width >= summed * stack[-1][1]:
            other, occurrences = stack.pop()
            summed += other
            width += occurrences
        stack.append((summed, width))
    return stack


# --- clause: main :: () -> None ---
def main():
    out = []
    for summed, width in flatten(read_input()):
        value = "%.9f" % (summed / width)
        for _ in range(width):
            out.append(value)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
