import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause wait_time [Confidence: 0.60]
def wait_time(year):
    digits = str(year)
    lead = int(digits[0]) + 1
    nxt = lead * 10 ** (len(digits) - 1)
    return nxt - year

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(str(wait_time(read_input())) + "\n")


if __name__ == "__main__":
    main()

