# resubmission retry after an unexplained RUNTIME_ERROR on a prior identical run
import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    asked = list(map(int, data[2:2 + n]))
    return n, k, asked

# Clause find_sector [Confidence: 1.00]
def find_sector(n, k, asked):
    index = k - 1
    while asked[index] == 0:
        index += 1
        if index == n:
            index = 0
    return index + 1

# Clause main [Confidence: 1.00]
def main():
    n, k, asked = read_input()
    sys.stdout.write(str(find_sector(n, k, asked)) + "\n")


if __name__ == "__main__":
    main()

