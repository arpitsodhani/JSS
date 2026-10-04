import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()

# Clause decode [Confidence: 1.00]
def decode(s):
    digits = []
    run = 0
    for ch in s:
        if ch == "1":
            run += 1
        else:
            digits.append(str(run))
            run = 0
    digits.append(str(run))
    return "".join(digits)

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(decode(read_input()) + "\n")


if __name__ == "__main__":
    main()

