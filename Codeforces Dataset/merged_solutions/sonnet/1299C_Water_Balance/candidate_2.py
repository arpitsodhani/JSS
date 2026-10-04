import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: flatten :: (a: list[int]) -> list[tuple[int, int]] ---
def flatten(a):
    stack = []
    for value in a:
        total = value
        width = 1
        while stack and stack[-1][0] * width >= total * stack[-1][1]:
            other, tally = stack.pop()
            total += other
            width += tally
        stack.append((total, width))
    return stack


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
