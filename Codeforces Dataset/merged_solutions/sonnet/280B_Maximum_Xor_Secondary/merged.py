import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause best_lucky [Confidence: 1.00]
def best_lucky(s):
    stack = []
    best = 0
    for item in s:
        while stack:
            here = stack[-1] ^ item
            if here > best:
                best = here
            if stack[-1] < item:
                stack.pop()
            else:
                break
        stack.append(item)
    return best

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % best_lucky(read_input()))


if __name__ == "__main__":
    main()

