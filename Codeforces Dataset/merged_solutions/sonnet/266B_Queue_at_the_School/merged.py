import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[1]), data[2].decode()

# Clause shuffle_queue [Confidence: 0.80]
def shuffle_queue(t, line):
    band = list(line)
    for _ in range(t):
        i = 0
        while i < len(band) - 1:
            if band[i] == "B" and band[i + 1] == "G":
                band[i] = "G"
                band[i + 1] = "B"
                i += 2
            else:
                i += 1
    return "".join(band)

# Clause main [Confidence: 1.00]
def main():
    t, line = read_input()
    sys.stdout.write(shuffle_queue(t, line) + "\n")


if __name__ == "__main__":
    main()

