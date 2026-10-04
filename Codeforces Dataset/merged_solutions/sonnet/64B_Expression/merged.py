import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().decode().strip()

# Clause evaluate [Confidence: 1.00]
def evaluate(line):
    begin = int(line[0])
    finish = int(line[2])
    if line[1] == "+":
        return begin + finish
    return begin - finish

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % evaluate(read_input()))


if __name__ == "__main__":
    main()

