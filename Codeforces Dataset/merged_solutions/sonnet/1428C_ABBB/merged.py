import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[1 + i].decode() for i in range(t)]

# Clause shortest_length [Confidence: 0.80]
def shortest_length(s):
    stack = 0
    begin = 0
    for ch in s:
        if ch == "A":
            stack += 1
            begin += 1
        elif stack or begin:
            if stack:
                stack -= 1
                begin -= 1
            else:
                begin -= 1
        else:
            begin += 1
    return begin

# Clause main [Confidence: 1.00]
def main():
    lines = []
    for s in read_input():
        lines.append(shortest_length(s))
    sys.stdout.write("\n".join(map(str, lines)) + "\n")


if __name__ == "__main__":
    main()

