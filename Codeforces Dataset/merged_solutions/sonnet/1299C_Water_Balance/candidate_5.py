import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: flatten :: (a: list[int]) -> list[tuple[int, int]] ---
def flatten(a):
    stack = []
    for value in a:
        running = value
        width = 1
        while stack and stack[-1][0] * width >= running * stack[-1][1]:
            other, hits = stack.pop()
            running += other
            width += hits
        stack.append((running, width))
    return stack


# --- clause: main :: () -> None ---
def main():
    out = []
    for running, width in flatten(read_input()):
        value = "%.9f" % (running / width)
        for _ in range(width):
            out.append(value)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
