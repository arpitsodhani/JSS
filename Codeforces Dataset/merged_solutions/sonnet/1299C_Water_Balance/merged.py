import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause flatten [Confidence: 0.80]
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

# Clause main [Confidence: 1.00]
def main():
    out = []
    for running, width in flatten(read_input()):
        value = "%.9f" % (running / width)
        for _ in range(width):
            out.append(value)
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

