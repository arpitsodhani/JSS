import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()

# Clause smallest_form [Confidence: 1.00]
def smallest_form(s):
    zeros = 0
    ones = 0
    for ch in s:
        if ch == "0":
            zeros += 1
        else:
            ones += 1
    if ones == 0:
        return "0"
    return "1" + "0" * zeros

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(smallest_form(read_input()) + "\n")


if __name__ == "__main__":
    main()

