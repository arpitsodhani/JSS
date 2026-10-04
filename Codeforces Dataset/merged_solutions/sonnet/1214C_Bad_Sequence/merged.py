import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()

# Clause nearly_correct [Confidence: 0.80]
def nearly_correct(s):
    balance = 0
    lowest = 0
    for ch in s:
        balance += 1 if ch == "(" else -1
        if balance < lowest:
            lowest = balance
    return balance == 0 and lowest >= -1

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("Yes\n" if nearly_correct(read_input()) else "No\n")


if __name__ == "__main__":
    main()

