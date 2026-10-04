import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# Clause fewest_replaces [Confidence: 0.80]
def fewest_replaces(s):
    pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    stack = []
    changes = 0
    for ch in s:
        if ch in pairs:
            if not stack:
                return -1
            if stack.pop() != pairs[ch]:
                changes += 1
        else:
            stack.append(ch)
    if stack:
        return -1
    return changes

# Clause main [Confidence: 1.00]
def main():
    answer = fewest_replaces(read_input())
    sys.stdout.write("Impossible\n" if answer < 0 else "%d\n" % answer)


if __name__ == "__main__":
    main()

