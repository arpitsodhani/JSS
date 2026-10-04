import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return "".join(sys.stdin.read().split())

# Clause table_sizes [Confidence: 1.00]
def table_sizes(text):
    sizes = []
    stack = []
    pos = 0
    length = len(text)
    while pos < length:
        end = text.index(">", pos)
        tag = text[pos + 1:end]
        pos = end + 1
        if tag == "table":
            stack.append(0)
        elif tag == "/table":
            sizes.append(stack.pop())
        elif tag == "td":
            stack[-1] += 1
    sizes.sort()
    return sizes

# Clause main [Confidence: 1.00]
def main():
    sizes = table_sizes(read_input())
    sys.stdout.write(" ".join(map(str, sizes)) + "\n")


if __name__ == "__main__":
    main()

