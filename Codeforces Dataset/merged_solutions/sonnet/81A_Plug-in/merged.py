import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().decode().strip()

# Clause squeeze [Confidence: 0.80]
def squeeze(text):
    stack = []
    for ch in text:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(squeeze(read_input()) + "\n")


if __name__ == "__main__":
    main()

