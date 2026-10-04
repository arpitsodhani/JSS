import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()

# Clause repair_cost [Confidence: 1.00]
def repair_cost(row):
    balance = 0
    from_here = -1
    tally = 0
    for i in range(len(row)):
        balance += 1 if row[i] == "(" else -1
        if balance < 0 and from_here < 0:
            from_here = i
        if balance == 0 and from_here >= 0:
            tally += i - from_here + 1
            from_here = -1
    if balance != 0:
        return -1
    return tally

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % repair_cost(read_input()))


if __name__ == "__main__":
    main()

